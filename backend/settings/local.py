# Import all settings from the base settings module
from .settings import *

# Define allowed hosts for the application
# Allow all hosts (not recommended for production)
ALLOWED_HOSTS: list[str] = ['*']

# CORS Configuration
# Define whether to allow all origins or specific ones
# Allow all origins (use with caution in production)
CORS_ALLOW_ALL_ORIGINS: bool = True

# Define specific CORS allowed origins (empty list since all origins are allowed)
# No specific origins are allowed when CORS_ALLOW_ALL_ORIGINS is True
CORS_ALLOWED_ORIGINS: list[str] = []
