from flask import Flask, jsonify, request
from mongo_client import get_collection

app = Flask(__name__)

# API route to add a name
@app.route('/api/add/<name>', methods=['POST'])
def add_name(name):
    try:
        collection = get_collection('mydatabase', 'names')  # Access the 'names' collection
        # Insert the name into the collection
        result = collection.insert_one({"name": name})

        # Return success response
        return jsonify({
            "message": f"Name '{name}' has been added successfully!",
            "id": str(result.inserted_id)
        }), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# API route to fetch all names (Updated as home route)
@app.route('/')
def home():
    try:
        collection = get_collection('mydatabase', 'names')  # Access the 'names' collection

        # Fetch all names from the collection
        names = []
        for doc in collection.find():  # Find all documents in the collection
            names.append(doc.get('name'))  # Get the 'name' field, handling possible missing fields

        # Return the names in JSON format
        return jsonify({"names": names})
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
