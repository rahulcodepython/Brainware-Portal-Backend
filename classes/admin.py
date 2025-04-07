"""
Django admin configuration for registering models with the admin interface.
This module defines how models are displayed and managed in the Django admin panel.
"""
from django.contrib import admin  # Import Django admin module
from .models import (  # Import models from the current app
    LecturePlan,
    Attendance,
    Class_Routine,
    Preparatory_Class
)


@admin.register(LecturePlan)
class LecturePlanAdmin(admin.ModelAdmin):
    """Admin configuration for the LecturePlan model."""
    # Define columns to display in the admin list view
    list_display: tuple[str, ...] = ('id', 'lecture', 'assigned_date')
    # Define fields to enable search functionality
    search_fields: tuple[str, ...] = ('id',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    """Admin configuration for the Attendance model."""
    # Define columns to display in the admin list view
    list_display: tuple[str, ...] = ('id', 'student', 'attendance_status')
    # Define fields to enable search functionality
    search_fields: tuple[str, ...] = ('id',)


@admin.register(Class_Routine)
class ClassRoutineAdmin(admin.ModelAdmin):
    """Admin configuration for the Class_Routine model."""
    # Define columns to display in the admin list view
    list_display: tuple[str, ...] = ('id', 'course', 'faculty')
    # Define fields to enable search functionality
    search_fields: tuple[str, ...] = ('id',)


@admin.register(Preparatory_Class)
class PreparatoryClassAdmin(admin.ModelAdmin):
    """Admin configuration for the Preparatory_Class model."""
    # Define columns to display in the admin list view
    list_display: tuple[str, ...] = ('id', 'class_routine', 'approved')
    # Define fields to enable search functionality
    search_fields: tuple[str, ...] = ('id',)
