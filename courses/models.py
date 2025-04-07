from django.db import models  # Importing Django's models module for ORM functionality
from typing import List  # Import typing for type hints


class Course(models.Model):
    """
    Model representing a Course with its properties and relationships.
    A Course can contain multiple Modules.
    """
    # Unique identifier for the course
    id: str = models.CharField(max_length=30, primary_key=True, unique=True)
    # Name of the course with a maximum length of 100 characters
    name: str = models.CharField(max_length=100)
    # Many-to-Many relationship with Module
    modules: List["Module"] = models.ManyToManyField(
        "Module", related_name="course_modules")

    def __str__(self) -> str:
        """Return string representation of the Course."""
        return self.id

    class Meta:
        """Meta class for Course model."""
        verbose_name_plural = "Courses"  # Plural name for the admin interface


class Module(models.Model):
    """
    Model representing a Module within a Course.
    A Module can contain multiple Lectures and belongs to a Course.
    """
    # Unique identifier for the module
    id: str = models.CharField(max_length=30, primary_key=True, unique=True)
    # Name of the module with a maximum length of 100 characters
    name: str = models.CharField(max_length=100)
    # ForeignKey relationship with Course
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    # Many-to-Many relationship with Lecture
    lectures: List["Lecture"] = models.ManyToManyField(
        "Lecture", related_name="module_lectures")

    def __str__(self) -> str:
        """Return string representation of the Module."""
        return self.id

    class Meta:
        """Meta class for Module model."""
        verbose_name_plural = "Modules"  # Plural name for the admin interface


class Lecture(models.Model):
    """
    Model representing a Lecture within a Module.
    Contains educational content and belongs to a Module.
    """
    # Unique identifier for the lecture
    id: str = models.CharField(max_length=30, primary_key=True, unique=True)
    # Name of the lecture with a maximum length of 100 characters
    name: str = models.CharField(max_length=100)
    # ForeignKey relationship with Module
    module = models.ForeignKey("Module", on_delete=models.CASCADE)
    # Text field to describe course outcomes
    course_outcome: str = models.TextField()

    def __str__(self) -> str:
        """Return string representation of the Lecture."""
        return self.id

    class Meta:
        """Meta class for Lecture model."""
        verbose_name_plural = "Lectures"  # Plural name for the admin interface
