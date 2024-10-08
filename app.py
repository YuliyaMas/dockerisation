"""Program for uploading users' files"""

from flask import Flask, request, redirect, url_for, render_template, flash
import os
import time
from werkzeug.utils import secure_filename

# Instantiate the Flask app
app = Flask(__name__)

# Create the folder for uploaded files
UPLOAD_FOLDER = 'uploads'

ALLOWED_EXTENSIONS = {'txt', 'docx', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'randomkeynumbersletters123'

# Check if upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def allowed_file(filename):
    """Check if the file has an allowed extension"""
    extension = filename.rsplit('.', 1)[1].lower()
    for allowed_ext in ALLOWED_EXTENSIONS:
        if extension == allowed_ext:
            return True
    return False


@app.route('/')
def upload_form():
    """Submit the file upload form"""
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle the upload"""
    if 'file' not in request.files:
        flash('No selected file')
        return redirect(request.url)

    file = request.files['file']

    # If user does not select a file
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Secure the filename
        filename = secure_filename(file.filename)
        # Create a unique subdirectory based on the current timestamp
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        upload_dir = os.path.join(app.config['UPLOAD_FOLDER'], timestamp)
        os.makedirs(upload_dir, exist_ok=True)

        # Save the file to the created directory
        file_path = os.path.join(upload_dir, filename)
        file.save(file_path)

        # Provide feedback on the type of file uploaded
        file_type = filename.rsplit('.', 1)[1].lower()
        flash(f'File "{filename}" uploaded successfully! Type: {file_type}')

        return redirect(url_for('upload_form'))
    else:
        flash('Invalid file type')
        return redirect(request.url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
