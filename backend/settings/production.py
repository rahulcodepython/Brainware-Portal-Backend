# Import all settings from the base settings module
from .settings import *

# Define allowed hosts for the application
# Restrict access to these hosts
ALLOWED_HOSTS: list[str] = ['localhost', '127.0.0.1']

# CORS Configuration
# Allow all origins for Cross-Origin Resource Sharing (CORS)
# Explicitly define allowed origins (currently empty)
CORS_ALLOWED_ORIGINS: list[str] = []
# Enable CORS for all origins (use cautiously in production)
CORS_ALLOW_ALL_ORIGINS: bool = True
