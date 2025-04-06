# For custom user model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models  # For database models
from .manager import UserCustomManager  # Custom manager for User model


# Custom User model inheriting from AbstractBaseUser and PermissionsMixin
class User(AbstractBaseUser, PermissionsMixin):
    # Unique identifier for the user
    code: str = models.CharField(max_length=20, unique=True)
    is_active: bool = models.BooleanField(
        default=True)  # Indicates if the user is active
    # Indicates if the user is a staff member
    is_staff: bool = models.BooleanField(default=False)

    # Custom manager for User model
    objects = UserCustomManager()

    # Field used for authentication
    USERNAME_FIELD: str = 'code'
    REQUIRED_FIELDS: list = []  # No additional required fields

    def __str__(self) -> str:
        return self.code  # String representation of the user


# Abstract Profile model to be inherited by specific profiles
class Profile(models.Model):
    # Unique code for the profile
    code: str = models.CharField(max_length=20, unique=True, primary_key=True)
    # One-to-one relationship with User
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    name: str = models.CharField(max_length=100)  # Name of the profile owner
    email: str = models.EmailField()  # Email of the profile owner

    # Gender choices for the profile
    GENDER_CHOICES: tuple = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender: str = models.CharField(
        max_length=10, choices=GENDER_CHOICES)  # Gender field with choices

    def __str__(self) -> str:
        return self.user.code  # String representation of the profile

    class Meta:
        abstract = True  # Marking this model as abstract


# Student Profile model inheriting from Profile
class Student_Profile(Profile):
    # Foreign key to Section model, allowing null and blank values
    section: models.ForeignKey = models.ForeignKey(
        "academics.Section", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.user.code  # String representation of the student profile

    class Meta:
        verbose_name: str = "Student Profile"  # Singular name for admin
        verbose_name_plural: str = "Student Profiles"  # Plural name for admin


# Faculty Profile model inheriting from Profile
class Faculty_Profile(Profile):
    # Foreign key to Department model, allowing null and blank values
    department: models.ForeignKey = models.ForeignKey(
        "academics.Department", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.user.code  # String representation of the faculty profile

    class Meta:
        verbose_name: str = "Faculty Profile"  # Singular name for admin
        verbose_name_plural: str = "Faculty Profiles"  # Plural name for admin
