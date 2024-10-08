# Dockerisation of the program for uploading files in various formats
## Features
Uploading files (.docx, .txt, .pdf, .png, .jpg, .jpeg, .gif).
Dockerising for easy deployment
Support of persistent file storage using Docker volumes

## Prerequisites
- **Docker** installed on your system.

## Quick Start

### 1. Build the Docker image:
bash:
docker build -t upload_files_flask .

### 2. Run the Docker container:
bash:
docker run -p 5000:5000 -v /path<here is your path to the storage on local disk>/uploads:/app/uploads upload_files_flask


### 3. Access the app:
Open a browser http://localhost:5000

## Project Structure
/dockerisation
  ├── app.py              # Flask app 
  ├── Dockerfile          # Docker configuration
  ├── requirements.txt    # Librairies
  └── templates/
      └── index.html      # HTML file with form
  ├── uploads/            # Uploaded files              


## Persistent Storage
Use the volume flag (`-v`) to ensure uploaded files are saved on the host:
bash:
docker run -p 5000:5000 -v /path/uploads:/app/uploads upload_files_flask



