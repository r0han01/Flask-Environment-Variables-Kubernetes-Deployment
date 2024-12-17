# Step 1: Use the official Python image as the base image
FROM python:3.12-alpine

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the entire backend application into the container
COPY . /app/

# Step 6: Expose the port the Flask app runs on (default 5000)
EXPOSE 5000

# Step 7: Set the environment variable for Flask to run in production mode (optional)
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Step 8: Run the Flask app when the container starts
CMD ["python", "app.py"]
