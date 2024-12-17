from pymongo import MongoClient

# MongoDB client setup
def get_mongo_client():
    # Connect to MongoDB without authentication (assuming MongoDB doesn't require login)
    client = MongoClient('mongodb://mongo.application-k8.svc.cluster.local:27017')  # Correct DNS name for MongoDB service in the Kubernetes cluster
    return client

def get_collection(db_name, collection_name):
    # Get MongoDB client
    client = get_mongo_client()
    # Access the database
    db = client[db_name]
    # Access the collection
    collection = db[collection_name]
    return collection
