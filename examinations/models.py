from django.db import models
from authentication.models import Student_Profile
from courses.models import Course
from academics.models import Semester

# Create your models here.


class Marks(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    student = models.ForeignKey(Student_Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    assignment1 = models.IntegerField()
    assignment2 = models.IntegerField()
    ppt = models.IntegerField()
    class_test1 = models.IntegerField()
    class_test2 = models.IntegerField()
    final = models.IntegerField()
    total = models.IntegerField()
    grade = models.CharField(max_length=2)
    percentage = models.FloatField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Marks'
        verbose_name_plural = 'Marks'
