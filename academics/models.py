from django.db import models  # Importing Django's models module for ORM functionality


# Department model to represent departments in the system
class Department(models.Model):
    # Unique identifier for the department
    id: models.CharField = models.CharField(
        max_length=30, primary_key=True, unique=True
    )
    # Name of the department
    name: models.CharField = models.CharField(max_length=100)
    # Many-to-Many relationship with Batch
    batches: models.ManyToManyField = models.ManyToManyField(
        "Batch", related_name="department_batches", blank=True
    )

    def __str__(self) -> str:
        # String representation of the department
        return f"{self.name}-{self.id}"

    class Meta:
        # Plural name for the admin interface
        verbose_name_plural = "Departments"


# Batch model to represent batches within a department
class Batch(models.Model):
    # Unique identifier for the batch
    id: models.CharField = models.CharField(
        max_length=30, primary_key=True, unique=True
    )
    # Name of the batch
    name: models.CharField = models.CharField(max_length=100)
    # ForeignKey relationship with Department
    department: models.ForeignKey = models.ForeignKey(
        "Department", on_delete=models.CASCADE
    )
    # Many-to-Many relationship with Section
    sections: models.ManyToManyField = models.ManyToManyField(
        "Section", related_name="batch_sections", blank=True
    )
    # Many-to-Many relationship with Semester
    semesters: models.ManyToManyField = models.ManyToManyField(
        "Semester", related_name="batch_semester", blank=True
    )
    # Current semester of the batch
    current_semester: models.ForeignKey = models.ForeignKey(
        "Semester",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="current_semester_batch",
    )

    def __str__(self) -> str:
        # String representation of the batch
        return self.id

    class Meta:
        # Plural name for the admin interface
        verbose_name_plural = "Batches"


# Section model to represent sections within a batch
class Section(models.Model):
    # Unique identifier for the section
    id: models.CharField = models.CharField(
        max_length=30, primary_key=True, unique=True
    )
    # Name of the section
    name: models.CharField = models.CharField(max_length=100)
    # ForeignKey relationship with Batch
    batch: models.ForeignKey = models.ForeignKey(
        "Batch", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        # String representation of the section
        return self.id

    class Meta:
        # Plural name for the admin interface
        verbose_name_plural = "Sections"


# Semester model to represent semesters within a batch
class Semester(models.Model):
    # Unique identifier for the semester
    id: models.CharField = models.CharField(
        max_length=30, primary_key=True, unique=True
    )
    # Name of the semester
    name: models.CharField = models.CharField(max_length=100)
    # ForeignKey relationship with Batch
    batch: models.ForeignKey = models.ForeignKey(
        "Batch", on_delete=models.CASCADE
    )
    # Many-to-Many relationship with Course
    courses: models.ManyToManyField = models.ManyToManyField(
        "courses.Course", related_name="semester_courses", blank=True
    )

    def __str__(self) -> str:
        # String representation of the semester
        return self.id

    class Meta:
        # Plural name for the admin interface
        verbose_name_plural = "Semesters"


# Semester_Course_Faculty model to represent faculty assignments to courses in a semester
class Semester_Course_Faculty(models.Model):
    # Unique identifier for the semester-course-faculty mapping
    id: models.CharField = models.CharField(
        max_length=30, primary_key=True, unique=True
    )
    # ForeignKey relationship with Semester
    semester: models.ForeignKey = models.ForeignKey(
        "Semester", on_delete=models.CASCADE
    )
    # ForeignKey relationship with Course
    course: models.ForeignKey = models.ForeignKey(
        "courses.Course", on_delete=models.CASCADE
    )
    # Many-to-Many relationship with Faculty_Profile
    faculty: models.ManyToManyField = models.ManyToManyField(
        "authentication.Faculty_Profile",
        blank=True,
        related_name="faculty_semester_courses",
    )

    def __str__(self) -> str:
        # String representation of the mapping
        return f"{self.semester.name}-{self.course.name}"

    def save(self, *args, **kwargs) -> None:
        # Automatically generate the ID if not provided
        if not self.id:
            self.id = f"{self.semester.id}-{self.course.id}"
        super().save(*args, **kwargs)  # Call the parent save method

        def clean(self):
            if not self.id:
                # Ensure the ID field is not required in the admin panel
                self.id = f"{self.semester.id}-{self.course.id}"

    class Meta:
        # Plural name for the admin interface
        verbose_name_plural = "Semester Course Faculty"
