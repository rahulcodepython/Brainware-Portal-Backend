from django.db import models  # Importing Django's ORM for database models


# Lecture Plan model to manage lecture schedules and details
class LecturePlan(models.Model):
    # Unique identifier for the lecture plan
    id: str = models.CharField(max_length=150, primary_key=True, unique=True)
    course: models.ForeignKey = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE)  # Associated course
    module: models.ForeignKey = models.ForeignKey(
        "courses.Module", on_delete=models.CASCADE)  # Associated module
    lecture: models.ForeignKey = models.ForeignKey(
        "courses.Lecture", on_delete=models.CASCADE)  # Associated lecture
    section: models.ForeignKey = models.ForeignKey(
        "academics.Section", on_delete=models.CASCADE)  # Associated section
    semester: models.ForeignKey = models.ForeignKey(
        "academics.Semester", on_delete=models.CASCADE)  # Associated semester
    referrence_class_routine: models.ForeignKey = models.ForeignKey(
        "Class_Routine", on_delete=models.SET_NULL, null=True, blank=True, default=None
    )  # Optional reference to class routine
    assigned_date: models.DateField = models.DateField()  # Date assigned
    assigned_faculties: models.ManyToManyField = models.ManyToManyField(
        "authentication.Faculty_Profile", related_name="lecture_plan_faculties"
    )  # Faculties assigned to the lecture plan
    assigned_room: str = models.CharField(max_length=100)  # Room assigned
    assigned_method: str = models.CharField(
        max_length=100)  # Teaching method assigned
    accomplision_status: bool = models.BooleanField(
        default=False)  # Status of accomplishment
    accomplished_date: models.DateField = models.DateField(
        null=True, blank=True)  # Date of accomplishment
    accomplished_faculties: models.ManyToManyField = models.ManyToManyField(
        "authentication.Faculty_Profile", related_name="lecture_plan_accomplished_faculties", blank=True
    )  # Faculties who accomplished the lecture
    accomplished_room: str = models.CharField(
        max_length=100, null=True, blank=True)  # Room used for accomplishment
    accomplished_method: str = models.CharField(
        max_length=100, null=True, blank=True)  # Method used for accomplishment

    def __str__(self) -> str:
        return self.id  # String representation of the lecture plan

    def save(self, *args, **kwargs) -> None:
        # Generate ID if not provided
        if not self.id:
            self.id = f"L-Plan-{self.module}-{self.lecture}-{self.referrence_class_routine}"
        super().save(*args, **kwargs)  # Save the model instance

    class Meta:
        verbose_name_plural = "Lecture Plans"  # Plural name for admin interface


# Attendance model to track student attendance
class Attendance(models.Model):
    # Unique identifier for attendance
    id: str = models.CharField(max_length=50, primary_key=True, unique=True)
    lecture_plan: models.ForeignKey = models.ForeignKey(
        "LecturePlan", on_delete=models.CASCADE)  # Associated lecture plan
    student: models.ForeignKey = models.ForeignKey(
        "authentication.Student_Profile", on_delete=models.CASCADE
    )  # Associated student
    attendance_status: bool = models.BooleanField(
        default=False)  # Attendance status (present/absent)
    attendance_date: models.DateField = models.DateField()  # Date of attendance

    def __str__(self) -> str:
        return self.id  # String representation of the attendance

    class Meta:
        verbose_name_plural = "Attendances"  # Plural name for admin interface


# Choices for days of the week
DAY_CHOICES: tuple = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)


# Class Routine model to manage class schedules
class Class_Routine(models.Model):
    # Unique identifier for the class routine
    id: str = models.CharField(max_length=50, primary_key=True, unique=True)
    section: models.ForeignKey = models.ForeignKey(
        "academics.Section", on_delete=models.CASCADE)  # Associated section
    semester: models.ForeignKey = models.ForeignKey(
        "academics.Semester", on_delete=models.CASCADE)  # Associated semester
    day: str = models.CharField(
        max_length=10, choices=DAY_CHOICES)  # Day of the week
    start_time: models.TimeField = models.TimeField()  # Start time of the class
    end_time: models.TimeField = models.TimeField()  # End time of the class
    course: models.ForeignKey = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE)  # Associated course
    faculty: models.ForeignKey = models.ForeignKey(
        "authentication.Faculty_Profile", on_delete=models.CASCADE
    )  # Faculty assigned to the class
    room: str = models.CharField(max_length=100)  # Room assigned for the class

    def __str__(self) -> str:
        return self.id  # String representation of the class routine

    def save(self, *args, **kwargs) -> None:
        # Validate that start time is before end time
        if self.start_time >= self.end_time:
            raise ValueError("Start time must be before end time.")

        # Generate ID if not provided
        if not self.id:
            self.id = f"{self.section}-{self.course}-{self.day}-{self.start_time.strftime('%H%M')}-{self.end_time.strftime('%H%M')}"
        super().save(*args, **kwargs)  # Save the model instance

    class Meta:
        verbose_name_plural = "Class Routines"  # Plural name for admin interface


# Preparatory Class model to manage substitute or preparatory classes
class Preparatory_Class(models.Model):
    # Unique identifier for the preparatory class
    id: str = models.CharField(max_length=50, primary_key=True, unique=True)
    class_routine: models.ForeignKey = models.ForeignKey(
        "Class_Routine", on_delete=models.CASCADE
    )  # Associated class routine
    new_faculty: models.ForeignKey = models.ForeignKey(
        "authentication.Faculty_Profile", on_delete=models.CASCADE
    )  # New faculty assigned to the class
    approved: bool = models.BooleanField(default=False)  # Approval status
    approved_date: models.DateField = models.DateField()  # Date of approval

    def __str__(self) -> str:
        return self.id  # String representation of the preparatory class

    class Meta:
        verbose_name_plural = "Preparatory Classes"  # Plural name for admin interface
