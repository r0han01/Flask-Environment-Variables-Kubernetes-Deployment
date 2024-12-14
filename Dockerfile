# Step 1: Use the Python image with Alpine base
FROM python:3.12-alpine

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the Flask app into the container
COPY . /app/

# Step 6: Expose the port the app runs on (default 8000)
EXPOSE 8000

# Step 7: Run the Flask app
CMD ["python", "app.py"]
