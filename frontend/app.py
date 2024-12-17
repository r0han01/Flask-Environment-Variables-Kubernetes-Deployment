from flask import Flask, render_template
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Get all environment variables as a dictionary
    env_vars = dict(os.environ)
    
    # Fetch names from the backend API running inside the Kubernetes cluster
    try:
        # Update the URL to point to the Kubernetes service for flask-backend
        response = requests.get('http://flask-backend.application-k8.svc.cluster.local:5000/')  # Correct backend URL
        names_data = response.json()  # Get names from the API response
        names = names_data.get('names', [])  # Extract names or an empty list if not found
    except requests.exceptions.RequestException as e:
        print(f"Error fetching names: {e}")
        names = []  # If the request fails, use an empty list of names

    # Pass both the environment variables and names to the template for rendering
    return render_template('index.html', env_vars=env_vars, names=names)

if __name__ == '__main__':
    # Get port from environment variable, default to 8000 if not found
    port = int(os.getenv('PORT', 8000))
    
    # Run the app on the specified port and make it accessible to other pods in the cluster
    app.run(debug=True, port=port, host='0.0.0.0')
