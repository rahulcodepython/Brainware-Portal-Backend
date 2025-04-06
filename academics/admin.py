# Importing admin module for Django admin interface
from django.contrib import admin
from .models import (  # Importing required models from the current app
    Department,
    Batch,
    Section,
    Semester,
    Semester_Course_Faculty,
)

# Registering models with the Django admin interface


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    # Displaying fields in the admin list view
    list_display: tuple[str, str] = ('id', 'name')
    # Enabling search functionality for specified fields
    search_fields: tuple[str, str] = ('id', 'name')


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    # Displaying fields in the admin list view
    list_display: tuple[str, str, str] = ('id', 'name', 'department')
    # Enabling search functionality for specified fields
    search_fields: tuple[str, str] = ('id', 'name')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    # Displaying fields in the admin list view
    list_display: tuple[str, str, str] = ('id', 'name', 'batch')
    # Enabling search functionality for specified fields
    search_fields: tuple[str, str] = ('id', 'name')


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    # Displaying fields in the admin list view
    list_display: tuple[str, str, str] = ('id', 'name', 'batch')
    # Enabling search functionality for specified fields
    search_fields: tuple[str, str] = ('id', 'name')


@admin.register(Semester_Course_Faculty)
class SemesterCourseFacultyAdmin(admin.ModelAdmin):
    # Displaying fields in the admin list view
    list_display: tuple[str, str, str] = ('id', 'semester', 'course')
    # Enabling search functionality for specified fields
    search_fields: tuple[str, str, str] = ('id', 'semester__id', 'course__id')
    # Adding filters for specified fields in the admin list view
    list_filter: tuple[str, str] = ('semester', 'course')
