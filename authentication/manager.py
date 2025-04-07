from django.contrib.auth.models import BaseUserManager
from typing import Optional, Any, TypeVar


class UserCustomManager(BaseUserManager):
    """
    Custom manager for User model that allows creating users with a code field
    instead of the standard username/email approach.
    """

    def create_user(self, code: str, password: Optional[str] = None, **extra_fields: Any) -> Any:
        """
        Create and save a regular user with the given code and password.

        Args:
            code: Unique identifier for the user
            password: Optional password for the user
            extra_fields: Additional fields to be set on the user model

        Returns:
            The created user instance

        Raises:
            ValueError: If the code field is not provided
        """
        # Ensure the 'code' field is provided
        if not code:
            raise ValueError("The code field must be set")

        # Create a user instance with the provided code and extra fields
        user = self.model(code=code, **extra_fields)

        # Set the user's password securely
        user.set_password(password)

        # Save the user instance to the database
        user.save(using=self._db)

        return user

    def create_superuser(self, code: str, password: Optional[str] = None, **extra_fields: Any) -> Any:
        """
        Create and save a superuser with the given code and password.

        Args:
            code: Unique identifier for the superuser
            password: Optional password for the superuser
            extra_fields: Additional fields to be set on the user model

        Returns:
            The created superuser instance

        Raises:
            ValueError: If is_staff or is_superuser is set to False
        """
        # Set default values for superuser-specific fields
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Extract the values for validation
        is_staff: bool = extra_fields.get('is_staff', False)
        is_superuser: bool = extra_fields.get('is_superuser', False)

        # Validate that the superuser-specific fields are correctly set
        if not is_staff:
            raise ValueError("Superuser must have is_staff=True.")
        if not is_superuser:
            raise ValueError("Superuser must have is_superuser=True.")

        # Create and return the superuser
        return self.create_user(code, password, **extra_fields)
