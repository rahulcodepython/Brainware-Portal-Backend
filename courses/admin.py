from django.contrib import admin  # Importing admin module to register models
# Importing models to be registered in the admin panel
from .models import Course, Module, Lecture


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Admin configuration for the Course model."""

    # Fields to display in the admin list view
    list_display: tuple[str, ...] = ('id', 'name')

    # Fields to enable search functionality
    search_fields: tuple[str, ...] = ('id', 'name')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    """Admin configuration for the Module model."""

    # Fields to display in the admin list view
    list_display: tuple[str, ...] = ('id', 'name', 'course')

    # Fields to enable search functionality
    search_fields: tuple[str, ...] = ('id', 'name')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    """Admin configuration for the Lecture model."""

    # Fields to display in the admin list view
    list_display: tuple[str, ...] = ('id', 'name', 'module')

    # Fields to enable search functionality
    search_fields: tuple[str, ...] = ('id', 'name')
