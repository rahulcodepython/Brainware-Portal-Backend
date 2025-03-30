from django.db import models
from courses.models import Course

# Create your models here.


class Department(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class Batch(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class Section(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    batch = models.ForeignKey("Batch", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class Semester(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    batch = models.ForeignKey("Batch", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class Semester_Course(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    semester = models.ForeignKey("Semester", on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course, related_name="semester_courses")

    def __str__(self):
        return self.id
