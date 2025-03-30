from django.db import models
from academics.models import Section
from courses.models import Course, Lecture
from authentication.models import Faculty_Profile, Student_Profile
# Create your models here.


class Lecture_Plan(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    assigned_date = models.DateField()
    assigned_faculties = models.ManyToManyField(
        Faculty_Profile, related_name="lecture_plan_faculties")
    assigned_room = models.CharField(max_length=100)
    assigned_method = models.CharField(max_length=100)
    accomplision_status = models.BooleanField(default=False)
    accomplished_date = models.DateField()
    accomplished_faculties = models.ManyToManyField(
        Faculty_Profile, related_name="lecture_plan_accomplished_faculties")
    accomplished_room = models.CharField(max_length=100)
    accomplished_method = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class Attendance(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    lecture_plan = models.ForeignKey("Lecture_Plan", on_delete=models.CASCADE)
    student = models.ForeignKey(Student_Profile, on_delete=models.CASCADE)
    attendance_status = models.BooleanField(default=False)
    attendance_date = models.DateField()

    def __str__(self):
        return self.id


DAY_CHOICES = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)


class Class_Routine(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty_Profile, on_delete=models.CASCADE)
    room = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class Preparatory_Class(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    class_routine = models.ForeignKey(
        "Class_Routine", on_delete=models.CASCADE)
    new_faculty = models.ForeignKey(
        Faculty_Profile, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    approved_date = models.DateField()

    def __str__(self):
        return self.id
