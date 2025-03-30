from dotenv import load_dotenv
import os

load_dotenv()

env = os.getenv("ENVIRONMENT", "development")

if env == "production":
    from .production import *
else:
    from .local import *
