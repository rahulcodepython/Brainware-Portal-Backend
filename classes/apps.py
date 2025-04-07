from django.apps import AppConfig


class ClassesConfig(AppConfig):
    """
    Configuration class for the 'classes' Django application.

    This class defines configuration parameters for the application
    including the default auto field type and application name.
    """
    default_auto_field: str = 'django.db.models.BigAutoField'  # Define the default auto field type for models
    name: str = 'classes'  # Define the name of the application
