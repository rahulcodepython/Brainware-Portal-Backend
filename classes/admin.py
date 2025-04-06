from django.contrib import admin  # Importing admin module to register models
from .models import (  # Importing required models from the current app
    LecturePlan,
    Attendance,
    Class_Routine,
    Preparatory_Class
)

# Registering LecturePlan model with custom admin configurations


@admin.register(LecturePlan)
class LecturePlanAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display: tuple[str, str, str] = ('id', 'lecture', 'assigned_date')
    # Fields to enable search functionality
    search_fields: tuple[str] = ('id',)

# Registering Attendance model with custom admin configurations


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display: tuple[str, str, str] = ('id', 'student', 'attendance_status')
    # Fields to enable search functionality
    search_fields: tuple[str] = ('id',)

# Registering Class_Routine model with custom admin configurations


@admin.register(Class_Routine)
class ClassRoutineAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display: tuple[str, str, str] = ('id', 'course', 'faculty')
    # Fields to enable search functionality
    search_fields: tuple[str] = ('id',)

# Registering Preparatory_Class model with custom admin configurations


@admin.register(Preparatory_Class)
class PreparatoryClassAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display: tuple[str, str, str] = ('id', 'class_routine', 'approved')
    # Fields to enable search functionality
    search_fields: tuple[str] = ('id',)
