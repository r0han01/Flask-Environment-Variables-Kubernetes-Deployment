from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get all environment variables as a dictionary
    env_vars = dict(os.environ)
    
    # Pass the dictionary to the template for rendering
    return render_template('index.html', env_vars=env_vars)

if __name__ == '__main__':
    # Get port from environment variable, default to 8000 if not found
    port = int(os.getenv('PORT', 8000))
    
    # Run the app on the specified port
    app.run(debug=True, port=port,host='0.0.0.0')
