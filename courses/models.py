from django.db import models  # Importing Django's models module for ORM functionality


# Model representing a Course
class Course(models.Model):
    id: str = models.CharField(
        max_length=30, primary_key=True, unique=True
    )  # Unique identifier for the course
    name: str = models.CharField(
        max_length=100
    )  # Name of the course with a maximum length of 100 characters
    modules: models.ManyToManyField = models.ManyToManyField(
        "Module", related_name="course_modules"
    )  # Many-to-Many relationship with Module

    def __str__(self) -> str:
        return self.id  # String representation of the course is its ID

    class Meta:
        verbose_name_plural = "Courses"  # Plural name for the admin interface


# Model representing a Module
class Module(models.Model):
    id: str = models.CharField(
        max_length=30, primary_key=True, unique=True
    )  # Unique identifier for the module
    name: str = models.CharField(
        max_length=100
    )  # Name of the module with a maximum length of 100 characters
    course: models.ForeignKey = models.ForeignKey(
        "Course", on_delete=models.CASCADE
    )  # ForeignKey relationship with Course, deletes module if course is deleted
    lectures: models.ManyToManyField = models.ManyToManyField(
        "Lecture", related_name="module_lectures"
    )  # Many-to-Many relationship with Lecture

    def __str__(self) -> str:
        return self.id  # String representation of the module is its ID

    class Meta:
        verbose_name_plural = "Modules"  # Plural name for the admin interface


# Model representing a Lecture
class Lecture(models.Model):
    id: str = models.CharField(
        max_length=30, primary_key=True, unique=True
    )  # Unique identifier for the lecture
    name: str = models.CharField(
        max_length=100
    )  # Name of the lecture with a maximum length of 100 characters
    module: models.ForeignKey = models.ForeignKey(
        "Module", on_delete=models.CASCADE
    )  # ForeignKey relationship with Module, deletes lecture if module is deleted
    # Text field to describe course outcomes
    course_outcome: str = models.TextField()

    def __str__(self) -> str:
        return self.id  # String representation of the lecture is its ID

    class Meta:
        verbose_name_plural = "Lectures"  # Plural name for the admin interface
