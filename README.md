# Flask Environment Variables and MongoDB Integration

This project demonstrates a Flask-based application that interacts with MongoDB to store and fetch names. The project consists of multiple services running in a Kubernetes environment, including a frontend and backend Flask app, MongoDB, and Mongo Express for database management.

## Project Structure

```plaintext
.
├── backend/
│   ├── app.py             # Flask backend app to handle API requests
│   ├── Dockerfile         # Dockerfile for the backend
│   ├── mongo_client.py    # MongoDB client connection setup
│   ├── requirements.txt   # Python dependencies for backend
│   └── venv/              # Python virtual environment for backend
├── frontend/
│   ├── app.py             # Flask frontend app to display environment variables and names
│   ├── Dockerfile         # Dockerfile for the frontend
│   ├── requirements.txt   # Python dependencies for frontend
│   ├── templates/         # HTML templates for frontend
│   └── venv/              # Python virtual environment for frontend
├── k8s/                   # Kubernetes YAML files for deployment
│   ├── backend.yaml       # Kubernetes configuration for backend
│   ├── frontend.yaml      # Kubernetes configuration for frontend
│   ├── mongo-express.yaml # Kubernetes configuration for Mongo Express
│   └── mongo.yaml         # Kubernetes configuration for MongoDB
└── README.md              # Project overview and setup guide
```
### Project Overview
This project demonstrates a simple environment where:

- Frontend: A Flask app that displays environment variables and fetches names from the backend API.
- Backend: A Flask app that interacts with a MongoDB database to store and retrieve names.
- MongoDB: A database used to store name records.
- Mongo Express: A web-based interface to interact with MongoDB.
The backend communicates with MongoDB via the `mongo-client.py file`, and the frontend fetches data from the backend API. All services are containerized using Docker and can be deployed to a Kubernetes cluster.

## Requirements
To run the application locally, you need the following:

- Python 3.12+
- Docker
- Kubernetes (Minikube or a cloud provider)
- MongoDB (or Mongo Express for the database UI)
- Setting Up Locally
## Step 1: Setup Virtual Environments
Create virtual environments for both the frontend and backend.

For backend:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
For frontend:

```bash
cd frontend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Step 2: Running the Backend
Start the Flask backend server by running:

```bash
cd backend
python app.py
```
By default, the backend will be accessible at ``http://127.0.0.1:5000.``

## Step 3: Running the Frontend
Start the Flask frontend server by running:

```bash
cd frontend
python app.py
```
By default, the frontend will be accessible at http://127.0.0.1:8000.

## Step 4: Dockerize the Applications
To build and run the backend Docker container:

```bash
cd backend
docker build -t r0han01/flask-backend .
docker run -p 5000:5000 r0han01/flask-backend
```
To build and run the frontend Docker container:

```bash
cd frontend
docker build -t r0han01/frontend .
docker run -p 8000:8000 r0han01/frontend
```
## Step 5: Accessing Mongo Express (Optional)
To run Mongo Express locally, you can pull and run the official Mongo Express Docker image:

```bash
docker run -d -p 8081:8081 --link mongo:mongodb mongo-express
```
This will allow you to interact with the MongoDB database through the web interface at `http://localhost:8081.`

# Kubernetes Deployment
The project is configured for deployment in a Kubernetes environment. The following services are defined in the k8s/ directory:

- MongoDB: The database service.
- Mongo Express: A web-based UI for MongoDB.
- Flask Backend: The API service that interacts with MongoDB.
- Frontend: The Flask app that fetches and displays data from the backend.
## Step 1: Deploy MongoDB
Apply the MongoDB configuration:

```bash
kubectl apply -f k8s/mongo.yaml
```
## Step 2: Deploy Mongo Express
Apply the Mongo Express configuration:

```bash
kubectl apply -f k8s/mongo-express.yaml
```
## Step 3: Deploy Backend
Apply the Flask backend deployment:

```bash
kubectl apply -f k8s/backend.yaml
```
## Step 4: Deploy Frontend
Apply the Flask frontend deployment:

```bash
kubectl apply -f k8s/frontend.yaml
```
##Step 5: Exposing Services
Ensure that the services are exposed and accessible through Kubernetes.

```bash
kubectl expose deployment flask-backend --type=LoadBalancer --name=flask-backend-service -n application-k8
kubectl expose deployment frontend --type=LoadBalancer --name=frontend-service -n application-k8
```
The frontend and backend services should now be accessible through the load balancer in your Kubernetes cluster.

## Accessing the Application
Once all the services are up, you can access:

- Frontend UI at http://<frontend-service-ip>:8000
- Backend API at http://<flask-backend-service-ip>:5000
- Mongo Express UI at http://<mongo-express-service-ip>:8081 (optional)
##Troubleshooting
- Backend Not Responding: Check the logs of the Flask backend to ensure there are no issues with MongoDB connectivity.
- MongoDB Connection: Ensure the MongoDB service is running and accessible by the Flask backend.
- Kubernetes Pods: Use kubectl get pods to check the status of the services.
```bash
kubectl get pods -n application-k8
```
# Continuation: Setup Instructions
### 1. Setting Up Kubernetes Cluster
If you haven't already set up a Kubernetes cluster, here are the steps to get started. You can use services like Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (EKS), or Minikube for local clusters.

Using Minikube (for local setup):
1. Install Minikube:

Follow the official Minikube installation guide to install Minikube.

For Ubuntu (example):

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https
sudo apt-get install -y minikube
```
2. Start Minikube Cluster:

Once installed, you can start a local cluster:

```bash
minikube start
```
Install kubectl (if not installed):

```bash
sudo apt-get install -y kubectl
```
Alternatively, you can use the kubectl provided by Minikube:

```bash
alias kubectl='minikube kubectl --'
```
Verify the Cluster is Running:

Run the following command to verify that your Kubernetes cluster is up and running:

```bash
kubectl cluster-info
```
### 2. Docker Setup
Ensure that Docker is installed on your machine for building images and running containers. For local testing, Docker is necessary to build the images for your backend, frontend, and MongoDB services.

Install Docker:
On Ubuntu:

```bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER  # Add the current user to the docker group
```
Build Docker Images:

Navigate to your project directories and build the Docker images for the frontend and backend services:

For the backend:

```bash
cd backend
docker build -t r0han01/flask-env-vars:latest .
```
For the frontend:

```bash
cd frontend
docker build -t r0han01/frontend:latest .
```

## Additional Considerations
### Logs
To view the logs of a specific pod, use the following command:

```bash
kubectl logs <pod-name> -n application-k8
```
Updating Deployments
When you update your Docker images or configuration, you can apply changes to your Kubernetes deployment:

```bash
kubectl apply -f backend.yaml
kubectl apply -f frontend.yaml
kubectl apply -f mongo-express.yaml
```
To ensure the latest image is used:

```bash
kubectl set image deployment/flask-backend flask-backend=r0han01/flask-env-vars:latest -n application-k8
```
Deleting Resources
If you need to clean up your Kubernetes resources:

```bash
kubectl delete -f backend.yaml
kubectl delete -f frontend.yaml
kubectl delete -f mongo-express.yaml
kubectl delete -f mongo.yaml
```
Troubleshooting
Pods Not Starting:

Check the status of the pod:
```bash
kubectl describe pod <pod-name> -n application-k8
```
View the logs of the failing pod:
```bash
kubectl logs <pod-name> -n application-k8
```
Service Issues:

Ensure the services are correctly set up:
```bash
kubectl get svc -n application-k8
```

## Interact with Flask API Using curl Inside the mongo-express Pod
### Explanation
- In this guide, we will interact with the Flask API inside your Kubernetes cluster using the `mongo-express` pod. We will perform two main tasks:

Add a name to the MongoDB database using the Flask API's `POST `endpoint.
Fetch all names stored in the database using the `GET` endpoint of the Flask API.
Here’s the step-by-step breakdown:

### Step 1: Enter the mongo-express Pod
We will start by entering the `mongo-express` pod, which provides a web interface to interact with the MongoDB instance in the cluster.

Run the following command to start an interactive shell session inside the `mongo-express` pod:

```bash
kubectl exec -it mongo-express-6c944bdb69-abcd9 -n application-k8 -- /bin/sh
```
### Explanation:
- `kubectl exec`: This command is used to run a command inside a pod.
- `-it`: Runs the shell interactively.
- `mongo-express-6c944bdb69-abcd9`: The pod name.
- `-n application-k8`: Specifies the Kubernetes namespace `(application-k8)`.
- `-- /bin/sh`: Opens a shell session in the pod.
This command opens a shell inside the pod, allowing you to run commands like curl to interact with the Flask API.

### Step 2: Use curl Inside the Pod to Interact with Flask API
#### Add a Name (POST request):
Now that we are inside the pod, we can use `curl` to make requests to the Flask API. The first request will be a `POST` request to add a name to the database. We will target the `flask-backend` service, which is running on port 5000 in the cluster.

Run the following `curl` command:

```bash
curl -X POST "http://flask-backend.application-k8:5000/api/add/John"
```
### Explanation:
- `curl -X POST`: The `curl` command with the `POST` method to send data.
- `"http://flask-backend.application-k8:5000/api/add/John":` The URL of the Flask API endpoint for adding a name. The name John is passed as a parameter in the URL.
### Expected response:
If the request is successful, you should get a response like this:

```json
{
  "message": "Name 'John' has been added successfully!",
  "id": "some-id-here"
}
```
### Fetch All Names (GET request):
Next, we'll send a `GET` request to retrieve all the names stored in the MongoDB database. The Flask API will return a list of names.

Run the following `curl` command:

```bash
curl "http://flask-backend.application-k8:5000/"
```
### Explanation:
- `curl`: The command to send a request.
- `"http://flask-backend.application-k8:5000/"`: The URL of the Flask API endpoint to fetch all names.
### Expected response:
The response will be a JSON list of all names stored in the database. For example:

```json
{
  "names": ["John", "Alice", "Bob"]
}
```
## Step 3: Update the curl Command to Add More Columns
### Adding More Columns (age, status, etc.):
You can easily extend the functionality to add additional fields (e.g., `age`, `status`) to the MongoDB document. Here's how to do it:

### Update the curl Command:
To add a name with additional fields (`age`, `status`), you need to send a JSON payload in the POST request. Here's how you can modify your `curl `command:

```bash
curl -X POST "http://flask-backend.application-k8:5000/api/add" \
    -H "Content-Type: application/json" \
    -d '{"name": "John", "age": 30, "status": "active"}'
```
### Explanation of the updated `curl` command:
- `-X POST`: The `POST `method for creating a new resource.
- `"http://flask-backend.application-k8:5000/api/add"`: The URL of the Flask API endpoint to add a name.
- `-H "Content-Type: application/json"`: Specifies that the request body is in JSON format.
- `-d '{"name": "John", "age": 30, "status": "active"}'`: Sends the data as JSON, where:
  - `name`: The name of the person to add.
  - `age`: The age of the person (you can replace 30 with any age).
  - `status`: The status of the person (e.g., "active", "inactive", etc.).
### Expected Response:
If the request is successful, the response will be similar to:

```json
{
  "message": "Name 'John' has been added successfully!",
  "id": "some-id-here"
}
```
Where `"some-id-here" `will be the unique ID assigned to the document in MongoDB.

### Summary of Changes:
- Flask API: The `POST `endpoint now accepts a JSON body with `name`, `age`, and `status` fields and stores them in the database.
- `curl` Command: We modified the `curl` command to send a JSON body with `name`, `age`, and `status` as part of the request.
## Step 4: Verify the Outputs
- For adding a name: If you successfully added a name, the response will confirm the addition, including the name and its unique ID in the database.
- For fetching names: The `GET` request should return a list of all names in the database.
## Step 5: Exit the Pod
After you’re done interacting with the pod, you can exit the shell session by typing `exit`:

```bash
exit
```
This will close the shell and bring you back to your local machine's terminal

## Conclusion
- This setup allows you to deploy a full-stack application (Flask backend, frontend, and MongoDB) in Kubernetes, with Docker images and services running in a cloud-native environment. Make sure you regularly update the deployments, monitor the services, and scale based on demand.
