from django.contrib.auth.models import BaseUserManager


class UserCustomManager(BaseUserManager):
    def create_user(self, code, password=None, **extra_fields):
        if not code:
            raise ValueError("The code field must be set")
        user = self.model(code=code, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, code, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(code, password, **extra_fields)
