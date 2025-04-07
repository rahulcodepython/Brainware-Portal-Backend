from django.db import models  # Importing Django's ORM for database models
from datetime import date, time  # Import date and time for type annotations
from typing import Optional, List, Any, Union  # Import type hints


class LecturePlan(models.Model):
    """
    Model to manage lecture schedules and details.
    Tracks planned lectures, their assignments and accomplishments.
    """
    # Unique identifier for the lecture plan
    id: str = models.CharField(max_length=150, primary_key=True, unique=True)
    # Associated course reference
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    # Associated module reference
    module = models.ForeignKey("courses.Module", on_delete=models.CASCADE)
    # Associated lecture reference
    lecture = models.ForeignKey("courses.Lecture", on_delete=models.CASCADE)
    # Associated section reference
    section = models.ForeignKey("academics.Section", on_delete=models.CASCADE)
    # Associated semester reference
    semester = models.ForeignKey(
        "academics.Semester", on_delete=models.CASCADE)
    # Optional reference to class routine
    referrence_class_routine = models.ForeignKey(
        "Class_Routine",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    # Date assigned for the lecture
    assigned_date: date = models.DateField()
    # Faculties assigned to the lecture plan
    assigned_faculties = models.ManyToManyField(
        "authentication.Faculty_Profile",
        related_name="lecture_plan_faculties"
    )
    # Room assigned for the lecture
    assigned_room: str = models.CharField(max_length=100)
    # Teaching method assigned
    assigned_method: str = models.CharField(max_length=100)
    # Status of accomplishment
    accomplision_status: bool = models.BooleanField(default=False)
    # Date of accomplishment (optional)
    accomplished_date: Optional[date] = models.DateField(null=True, blank=True)
    # Faculties who accomplished the lecture (optional)
    accomplished_faculties = models.ManyToManyField(
        "authentication.Faculty_Profile",
        related_name="lecture_plan_accomplished_faculties",
        blank=True
    )
    # Room used for accomplishment (optional)
    accomplished_room: Optional[str] = models.CharField(
        max_length=100, null=True, blank=True)
    # Method used for accomplishment (optional)
    accomplished_method: Optional[str] = models.CharField(
        max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        """Return string representation of the lecture plan"""
        return self.id

    def save(self, *args: Any, **kwargs: Any) -> None:
        """
        Save the lecture plan instance, generating ID if not provided.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments
        """
        # Generate ID if not provided
        if not self.id:
            # Create a descriptive ID based on related fields
            plan_id = f"L-Plan-{self.module}-{self.lecture}-{self.referrence_class_routine}"
            self.id = plan_id
        # Call the parent class's save method
        super().save(*args, **kwargs)

    class Meta:
        """Meta options for the LecturePlan model"""
        verbose_name_plural = "Lecture Plans"


class Attendance(models.Model):
    """
    Model to track student attendance for specific lecture plans.
    """
    # Unique identifier for attendance
    id: str = models.CharField(max_length=50, primary_key=True, unique=True)
    # Associated lecture plan reference
    lecture_plan = models.ForeignKey("LecturePlan", on_delete=models.CASCADE)
    # Associated student reference
    student = models.ForeignKey(
        "authentication.Student_Profile", on_delete=models.CASCADE)
    # Attendance status (present/absent)
    attendance_status: bool = models.BooleanField(default=False)
    # Date of attendance
    attendance_date: date = models.DateField()

    def __str__(self) -> str:
        """Return string representation of the attendance record"""
        return self.id

    class Meta:
        """Meta options for the Attendance model"""
        verbose_name_plural = "Attendances"


# Choices for days of the week
DAY_CHOICES: tuple = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
)


class Class_Routine(models.Model):
    """
    Model to manage class schedules with specific time slots, rooms, and faculty assignments.
    """
    # Unique identifier for the class routine
    id: str = models.CharField(max_length=50, primary_key=True, unique=True)
    # Associated section reference
    section = models.ForeignKey("academics.Section", on_delete=models.CASCADE)
    # Associated semester reference
    semester = models.ForeignKey(
        "academics.Semester", on_delete=models.CASCADE)
    # Day of the week
    day: str = models.CharField(max_length=10, choices=DAY_CHOICES)
    # Start time of the class
    start_time: time = models.TimeField()
    # End time of the class
    end_time: time = models.TimeField()
    # Associated course reference
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    # Faculty assigned to the class
    faculty = models.ForeignKey(
        "authentication.Faculty_Profile", on_delete=models.CASCADE)
    # Room assigned for the class
    room: str = models.CharField(max_length=100)

    def __str__(self) -> str:
        """Return string representation of the class routine"""
        return self.id

    def save(self, *args: Any, **kwargs: Any) -> None:
        """
        Save the class routine instance, validating times and generating ID if needed.

        Args:
            *args: Variable length argument list
            **kwargs: Arbitrary keyword arguments

        Raises:
            ValueError: If start time is not before end time
        """
        # Validate that start time is before end time
        if self.start_time >= self.end_time:
            raise ValueError("Start time must be before end time.")

        # Generate ID if not provided
        if not self.id:
            # Format times as strings for the ID
            start_time_str = self.start_time.strftime('%H%M')
            end_time_str = self.end_time.strftime('%H%M')
            # Create a descriptive ID based on related fields
            routine_id = f"{self.section}-{self.course}-{self.day}-{start_time_str}-{end_time_str}"
            self.id = routine_id

        # Call the parent class's save method
        super().save(*args, **kwargs)

    class Meta:
        """Meta options for the Class_Routine model"""
        verbose_name_plural = "Class Routines"


class Preparatory_Class(models.Model):
    """
    Model to manage substitute or preparatory classes when regular faculty is unavailable.
    """
    # Unique identifier for the preparatory class
    id: str = models.CharField(max_length=50, primary_key=True, unique=True)
    # Associated class routine reference
    class_routine = models.ForeignKey(
        "Class_Routine", on_delete=models.CASCADE)
    # New faculty assigned to the class
    new_faculty = models.ForeignKey(
        "authentication.Faculty_Profile", on_delete=models.CASCADE)
    # Approval status
    approved: bool = models.BooleanField(default=False)
    # Date of approval
    approved_date: date = models.DateField()

    def __str__(self) -> str:
        """Return string representation of the preparatory class"""
        return self.id

    class Meta:
        """Meta options for the Preparatory_Class model"""
        verbose_name_plural = "Preparatory Classes"
