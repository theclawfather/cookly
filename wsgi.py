# Cookly WSGI Configuration for PythonAnywhere
# International AI of Mystery 🕶️
# Created by @theclawdfather

import os
import sys

# Add the project directory to the path
path = '/home/YOUR_USERNAME/cookly'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = ''  # Not using Django
os.environ['FLASK_ENV'] = 'production'

# Import the Flask app
from app import app as application

# Configure for PythonAnywhere
if __name__ == "__main__":
    # This is used when running locally only
    application.run()