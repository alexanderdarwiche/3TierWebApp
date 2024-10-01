# Dockerfile for backend (Flask)
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variables (these can be passed via Azure later)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app with retry mechanism to make sure mysql container is ready before running the backend.
CMD ["sh", "-c", "while ! nc -z mysql-container 3306; do sleep 1; done; flask run"]
