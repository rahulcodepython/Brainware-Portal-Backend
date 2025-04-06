from django.contrib import admin  # Importing admin module to register models
# Importing models to be registered in the admin panel
from .models import Course, Module, Lecture

# Registering the Course model with custom admin configurations


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display: tuple[str, str] = ('id', 'name')
    # Fields to enable search functionality
    search_fields: tuple[str, str] = ('id', 'name')

# Registering the Module model with custom admin configurations


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display: tuple[str, str, str] = ('id', 'name', 'course')
    # Fields to enable search functionality
    search_fields: tuple[str, str] = ('id', 'name')

# Registering the Lecture model with custom admin configurations


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display: tuple[str, str, str] = ('id', 'name', 'module')
    # Fields to enable search functionality
    search_fields: tuple[str, str] = ('id', 'name')
