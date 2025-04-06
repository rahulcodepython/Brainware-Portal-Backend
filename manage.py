#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os  # Importing the os module for environment variable management
import sys  # Importing the sys module for command-line argument handling


def main() -> None:
    """Run administrative tasks."""
    # Setting the default Django settings module environment variable
    django_settings_module: str = 'backend.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_settings_module)

    try:
        # Importing the Django management command execution function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raising an error if Django is not installed or not available
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your "
            "PYTHONPATH environment variable. Did you forget to activate a virtual environment?"
        ) from exc

    # Executing the command-line arguments using Django's management utility
    execute_from_command_line(sys.argv)


# Entry point of the script
if __name__ == '__main__':
    main()
