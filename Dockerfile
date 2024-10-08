# Use the official Python image from the Docker Hub
FROM python:3.11-slim
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file and install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
# Copy the application code into the container
COPY . /app
# Expose port 5000
EXPOSE 5000
# Command to run the Flask app
CMD ["python", "app.py"]
