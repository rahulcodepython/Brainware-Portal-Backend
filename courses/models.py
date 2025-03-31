from django.db import models

# Create your models here.


class Course(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    modules = models.ManyToManyField("Module", related_name="course_modules")

    def __str__(self):
        return self.id


class Module(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    lectures = models.ManyToManyField(
        "Lecture", related_name="module_lectures")

    def __str__(self):
        return self.id


class Lecture(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    module = models.ForeignKey("Module", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    course_outcome = models.TextField()

    def __str__(self):
        return self.id
