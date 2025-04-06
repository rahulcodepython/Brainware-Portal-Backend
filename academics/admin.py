from django.contrib import admin
from .models import (
    Department, Batch, Section, Semester, Semester_Course_Faculty,
)

# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'department')
    search_fields = ('id', 'name')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'batch')
    search_fields = ('id', 'name')


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'batch')
    search_fields = ('id', 'name')


@admin.register(Semester_Course_Faculty)
class SemesterCourseFacultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'semester', 'course')
    search_fields = ('id', 'semester__id', 'course__id')
    list_filter = ('semester', 'course')
