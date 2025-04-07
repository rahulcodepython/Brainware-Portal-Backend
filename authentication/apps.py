from django.apps import AppConfig
from typing import ClassVar


class AuthenticationConfig(AppConfig):
    """
    Configuration class for the Authentication application.

    This class defines metadata for the Authentication app in Django.
    """
    # Define the default primary key field type for models
    default_auto_field: ClassVar[str] = 'django.db.models.BigAutoField'

    # Define the application name
    name: ClassVar[str] = 'authentication'
