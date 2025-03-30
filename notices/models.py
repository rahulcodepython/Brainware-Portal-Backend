from django.db import models
from authentication.models import Faculty_Profile

# Create your models here.


class Notice(models.Model):
    id = models.CharField(max_length=10, primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    uploaded_by = models.ForeignKey(
        Faculty_Profile, on_delete=models.CASCADE)
    document = models.FileField(
        upload_to='notice_files/', null=True, blank=True)

    def __str__(self):
        return self.title
