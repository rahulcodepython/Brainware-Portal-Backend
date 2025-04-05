from django.db import models

# Create your models here.


class Course(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    modules = models.ManyToManyField("Module", related_name="course_modules")

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Courses"


class Module(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    lectures = models.ManyToManyField(
        "Lecture", related_name="module_lectures")

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Modules"


class Lecture(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    module = models.ForeignKey("Module", on_delete=models.CASCADE)
    course_outcome = models.TextField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Lectures"
