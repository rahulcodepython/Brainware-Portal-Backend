from django.apps import AppConfig
from typing import ClassVar


class CoursesConfig(AppConfig):
    """
    Configuration class for the 'courses' Django application.

    This class specifies configuration attributes for the courses app including
    the default auto field and application name.
    """
    # The default auto field used for database primary keys
    default_auto_field: ClassVar[str] = 'django.db.models.BigAutoField'
    # The name of the Django application
    name: ClassVar[str] = 'courses'
