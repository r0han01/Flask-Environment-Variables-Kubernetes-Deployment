# Flask Environment Variables Web App

This is a simple Flask web application that lists all environment variables in a user-friendly format. It is Dockerized for easy deployment and can be configured via the `PORT` environment variable.

## Features
- Displays all environment variables passed to the Flask application.
- Clean and responsive UI built with Bootstrap 5.
- Configurable port through environment variable (`PORT`).

## Technologies
- **Flask**: Python web framework for building the application.
- **Docker**: Containerization for easy deployment.
- **Bootstrap 5**: Frontend framework for responsive styling.

## Flask Application Code (`app.py`)

The key parts of the Flask application are:

- **index() route**: Grabs all environment variables using `os.environ` and passes them to the template.
- **Dynamic port**: The port is set dynamically from the `PORT` environment variable, defaulting to 8000 if not found.
- **Rendering environment variables**: The environment variables are displayed in a nice list using the `index.html` template.

### Example Code (`app.py`)

```python
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
    app.run(debug=True, port=port, host='0.0.0.0')
```    
## Dockerfile

This Dockerfile sets up the containerized environment for the Flask application.

```bash
# Step 1: Use the Python image with Alpine base
FROM python:3.12-alpine

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Step 4: Install Python dependencies into a virtual environment
RUN python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the Flask app into the container
COPY . /app/

# Step 6: Set the environment variable for Flask to run
ENV PATH="/venv/bin:$PATH"

# Step 7: Expose the port the app runs on (default 8000)
EXPOSE 8000

# Step 8: Run the Flask app
CMD ["python", "app.py"]
```
### Explanation:
- Virtual Environment: The dependencies are installed into a virtual environment to isolate them from the base system.
- Flask App Port: The port is exposed as 8000, matching the Flask app configuration.
- Running the Flask app: The CMD directive runs app.py when the container starts.
## Optional: `.dockerignore`

To avoid copying unnecessary files (e.g., `venv/`, `.git/`), create a `.dockerignore` file with the following content:
```bash
venv/
__pycache__/
*.pyc
.git/
.idea/
```
Requirements
Make sure that your `requirements.txt` file contains the necessary dependencies for the Flask app.

Example `requirements.txt`
```bash
Flask==2.3.2
gunicorn==20.1.0  # Optional for production
```
If you're using `gunicorn` for production, be sure to include it in your `requirements.txt.`

## Build and Run the Application in Docker
1. Build the Docker Image
- To build the Docker image, run:

```bash
docker build -t flask-env-vars .
```
2. Run the Docker Container
- After building the image, run the container with:

```bash
docker run -p 8000:8000 flask-env-vars
```
3. Access the Application
- Visit http://localhost:8000 in your browser, and you should see the environment variables listed on the page.

### Additional Configuration
- Setting the PORT Environment Variable
You can configure the port by setting the PORT environment variable:

In the Dockerfile:

```bash
ENV PORT=8000
```
When running the container:

```bash
docker run -e PORT=8000 -p 8000:8000 flask-env-vars
```


