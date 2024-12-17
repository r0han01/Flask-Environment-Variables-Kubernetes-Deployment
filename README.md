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

## Conclusion
- This setup allows you to deploy a full-stack application (Flask backend, frontend, and MongoDB) in Kubernetes, with Docker images and services running in a cloud-native environment. Make sure you regularly update the deployments, monitor the services, and scale based on demand.