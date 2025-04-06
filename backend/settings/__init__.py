# Importing dotenv to load environment variables from a .env file
from dotenv import load_dotenv
import os  # Importing os to interact with the operating system

# Load environment variables from the .env file
load_dotenv()

# Define the type of the environment variable
# Get the "ENVIRONMENT" variable, default to "development"
env: str = os.getenv("ENVIRONMENT", "development")

try:
    # Check the environment and import the appropriate settings
    if env == "production":
        from .production import *  # Import production settings if environment is "production"
    else:
        from .local import *  # Import local settings for any other environment
except ImportError as e:
    # Handle ImportError if the specified settings file is not found
    raise ImportError(f"Error importing settings for environment '{env}': {e}")
