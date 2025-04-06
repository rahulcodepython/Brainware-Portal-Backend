from django.db import models

# Create your models here.


class Department(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    batches = models.ManyToManyField(
        "Batch", related_name="department_batches", blank=True)

    def __str__(self):
        return f"{self.name}-{self.id}"

    class Meta:
        verbose_name_plural = "Departments"


class Batch(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    sections = models.ManyToManyField(
        "Section", related_name="batch_sections", blank=True)
    semesters = models.ManyToManyField(
        "Semester", related_name="batch_semester", blank=True)
    current_semester = models.ForeignKey(
        "Semester", on_delete=models.CASCADE, null=True, blank=True, related_name="current_semester_batch")

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Batches"


class Section(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    batch = models.ForeignKey("Batch", on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Sections"


class Semester(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    batch = models.ForeignKey("Batch", on_delete=models.CASCADE)
    courses = models.ManyToManyField(
        "courses.Course", related_name="semester_courses", blank=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Semesters"


class Semester_Course_Faculty(models.Model):
    id = models.CharField(max_length=30, primary_key=True, unique=True)
    semester = models.ForeignKey("Semester", on_delete=models.CASCADE)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    faculty = models.ManyToManyField(
        "authentication.Faculty_Profile", blank=True, related_name="faculty_semester_courses")

    def __str__(self):
        return f"{self.semester.name}-{self.course.name}"

    def save(self, *args, **kwargs):
        if self.id is None:
            self.id = f"{self.semester.id}-{self.course.id}"

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Semester Course Faculty"
