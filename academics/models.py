from django.db import models  # Importing Django's models module for ORM functionality


# Department model to represent departments in the system
class Department(models.Model):
    id: str = models.CharField(
        # Unique identifier for the department
        max_length=30, primary_key=True, unique=True)
    name: str = models.CharField(max_length=100)  # Name of the department
    batches: models.ManyToManyField = models.ManyToManyField(
        # Many-to-Many relationship with Batch
        "Batch", related_name="department_batches", blank=True)

    def __str__(self) -> str:
        # String representation of the department
        return f"{self.name}-{self.id}"

    class Meta:
        verbose_name_plural = "Departments"  # Plural name for the admin interface


# Batch model to represent batches within a department
class Batch(models.Model):
    id: str = models.CharField(
        max_length=30, primary_key=True, unique=True)  # Unique identifier for the batch
    name: str = models.CharField(max_length=100)  # Name of the batch
    department: models.ForeignKey = models.ForeignKey(
        # ForeignKey relationship with Department
        "Department", on_delete=models.CASCADE)
    sections: models.ManyToManyField = models.ManyToManyField(
        # Many-to-Many relationship with Section
        "Section", related_name="batch_sections", blank=True)
    semesters: models.ManyToManyField = models.ManyToManyField(
        # Many-to-Many relationship with Semester
        "Semester", related_name="batch_semester", blank=True)
    current_semester: models.ForeignKey = models.ForeignKey(
        # Current semester of the batch
        "Semester", on_delete=models.CASCADE, null=True, blank=True, related_name="current_semester_batch")

    def __str__(self) -> str:
        return self.id  # String representation of the batch

    class Meta:
        verbose_name_plural = "Batches"  # Plural name for the admin interface


# Section model to represent sections within a batch
class Section(models.Model):
    id: str = models.CharField(
        # Unique identifier for the section
        max_length=30, primary_key=True, unique=True)
    name: str = models.CharField(max_length=100)  # Name of the section
    batch: models.ForeignKey = models.ForeignKey(
        "Batch", on_delete=models.CASCADE)  # ForeignKey relationship with Batch

    def __str__(self) -> str:
        return self.id  # String representation of the section

    class Meta:
        verbose_name_plural = "Sections"  # Plural name for the admin interface


# Semester model to represent semesters within a batch
class Semester(models.Model):
    id: str = models.CharField(
        # Unique identifier for the semester
        max_length=30, primary_key=True, unique=True)
    name: str = models.CharField(max_length=100)  # Name of the semester
    batch: models.ForeignKey = models.ForeignKey(
        "Batch", on_delete=models.CASCADE)  # ForeignKey relationship with Batch
    courses: models.ManyToManyField = models.ManyToManyField(
        # Many-to-Many relationship with Course
        "courses.Course", related_name="semester_courses", blank=True)

    def __str__(self) -> str:
        return self.id  # String representation of the semester

    class Meta:
        verbose_name_plural = "Semesters"  # Plural name for the admin interface


# Semester_Course_Faculty model to represent faculty assignments to courses in a semester
class Semester_Course_Faculty(models.Model):
    id: str = models.CharField(
        # Unique identifier for the semester-course-faculty mapping
        max_length=30, primary_key=True, unique=True)
    semester: models.ForeignKey = models.ForeignKey(
        "Semester", on_delete=models.CASCADE)  # ForeignKey relationship with Semester
    course: models.ForeignKey = models.ForeignKey(
        # ForeignKey relationship with Course
        "courses.Course", on_delete=models.CASCADE)
    faculty: models.ManyToManyField = models.ManyToManyField(
        # Many-to-Many relationship with Faculty_Profile
        "authentication.Faculty_Profile", blank=True, related_name="faculty_semester_courses")

    def __str__(self) -> str:
        # String representation of the mapping
        return f"{self.semester.name}-{self.course.name}"

    def save(self, *args, **kwargs) -> None:
        # Automatically generate the ID if not provided
        if not self.id:
            self.id = f"{self.semester.id}-{self.course.id}"
        super().save(*args, **kwargs)  # Call the parent save method

    class Meta:
        # Plural name for the admin interface
        verbose_name_plural = "Semester Course Faculty"
