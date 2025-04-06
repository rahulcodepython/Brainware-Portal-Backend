# Utility to generate random secret keys
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv  # For loading environment variables from .env file
from datetime import timedelta  # For token expiration settings
from pathlib import Path  # For handling file paths
import os  # For accessing environment variables

# Load environment variables from .env file
load_dotenv()

# Base directory of the project
BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent

# Secret key for the application, generated if not provided in the environment
SECRET_KEY: str = os.getenv('SECRET_KEY', get_random_secret_key())

# Debug mode, enabled only in development environment
ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'development')
DEBUG: bool = ENVIRONMENT == 'development'

# Installed applications for the Django project
INSTALLED_APPS: list[str] = [
    'django.contrib.admin',  # Admin site
    'django.contrib.auth',  # Authentication framework
    'django.contrib.contenttypes',  # Content types framework
    'django.contrib.sessions',  # Session framework
    'django.contrib.messages',  # Messaging framework
    'django.contrib.staticfiles',  # Static files handling

    # Third-party apps
    'rest_framework',  # Django REST framework
    'corsheaders',  # Cross-Origin Resource Sharing
    'rest_framework_simplejwt',  # JWT authentication

    # Custom Django apps
    'academics',
    'authentication',
    'classes',
    'courses',
    'examinations',
    'notices',
]

# Middleware for handling requests and responses
MIDDLEWARE: list[str] = [
    'django.middleware.security.SecurityMiddleware',  # Security enhancements
    'django.contrib.sessions.middleware.SessionMiddleware',  # Session handling
    'corsheaders.middleware.CorsMiddleware',  # CORS handling
    'django.middleware.common.CommonMiddleware',  # Common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    # Authentication middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',  # Messaging middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
]

# Root URL configuration
ROOT_URLCONF: str = 'backend.urls'

# Template settings
TEMPLATES: list[dict] = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Template engine
        'DIRS': [],  # Directories for custom templates
        'APP_DIRS': True,  # Enable app directories for templates
        'OPTIONS': {
            'context_processors': [  # Context processors for templates
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application entry point
WSGI_APPLICATION: str = 'backend.wsgi.application'

# Custom user model
AUTH_USER_MODEL: str = 'authentication.User'

# Database configuration
DATABASES: dict = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # SQLite database engine
        'NAME': BASE_DIR / 'db.sqlite3',  # Database file path
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS: list[dict] = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE: str = 'en-us'  # Default language
TIME_ZONE: str = 'UTC'  # Default timezone
USE_I18N: bool = True  # Enable internationalization
USE_TZ: bool = True  # Enable timezone support

# Static files settings
STATIC_URL: str = 'static/'  # URL for serving static files

# Default primary key field type
DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'

# Django REST framework settings
REST_FRAMEWORK: dict = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # Default permission class
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT authentication
    )
}

# Simple JWT settings
ACCESS_TOKEN_LIFETIME: timedelta = timedelta(days=7)  # Access token lifetime
REFRESH_TOKEN_LIFETIME: timedelta = timedelta(
    days=14)  # Refresh token lifetime
SIMPLE_JWT: dict = {
    'ACCESS_TOKEN_LIFETIME': ACCESS_TOKEN_LIFETIME,
    'SLIDING_TOKEN_REFRESH_LIFETIME': REFRESH_TOKEN_LIFETIME,
    'AUTH_HEADER_TYPES': ('Bearer',),  # Authorization header type
}
