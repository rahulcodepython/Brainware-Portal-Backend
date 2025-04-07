from django.apps import AppConfig  # Importing AppConfig from Django apps module


# Defining the configuration class for the 'academics' app
class AcademicsConfig(AppConfig):
    # Setting the default auto field type for models in this app
    default_auto_field: str = 'django.db.models.BigAutoField'

    # Defining the name of the app
    name: str = 'academics'
