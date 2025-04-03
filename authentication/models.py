from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .manager import UserCustomManager
from academics.models import Department, Section, Semester


class User(AbstractBaseUser, PermissionsMixin):
    code = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserCustomManager()

    USERNAME_FIELD = 'code'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.code


class Profile(models.Model):
    code = models.CharField(max_length=20, unique=True, primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=(
        ('Male', 'Male'), ('Female', 'Female')))

    def __str__(self):
        return self.user

    class Meta:
        abstract = True


class Student_Profile(Profile):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, null=True, blank=True)
    current_semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.code


class Faculty_Profile(Profile):
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.code
