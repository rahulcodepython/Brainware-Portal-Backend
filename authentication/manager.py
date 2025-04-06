from django.contrib.auth.models import BaseUserManager
from typing import Optional, Any


class UserCustomManager(BaseUserManager):
    # Method to create a regular user
    def create_user(self, code: str, password: Optional[str] = None, **extra_fields: Any) -> Any:
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

    # Method to create a superuser
    def create_superuser(self, code: str, password: Optional[str] = None, **extra_fields: Any) -> Any:
        # Set default values for superuser-specific fields
        is_staff: bool = extra_fields.setdefault('is_staff', True)
        is_superuser: bool = extra_fields.setdefault('is_superuser', True)

        # Validate that the superuser-specific fields are correctly set
        if not is_staff:
            raise ValueError("Superuser must have is_staff=True.")
        if not is_superuser:
            raise ValueError("Superuser must have is_superuser=True.")

        # Create and return the superuser
        return self.create_user(code, password, **extra_fields)
