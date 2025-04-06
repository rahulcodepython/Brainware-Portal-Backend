from typing import Tuple  # For type annotations
from .models import User, Student_Profile, Faculty_Profile  # Importing models
# Importing Django's Group model
from django.contrib.auth.models import Group as DjangoGroup
from django.contrib import admin  # Importing admin module for model registration

# Setting up the admin panel's header and title
admin.site.site_header = 'Brainware University'  # Custom header for admin panel
admin.site.site_title = 'Brainware University'  # Custom title for admin panel

# Unregistering the default Django Group model from admin
admin.site.unregister(DjangoGroup)

# Admin configuration for the User model


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display: Tuple[str, str, str, str] = (
        'code', 'is_superuser', 'is_active', 'is_staff')
    # Fields to enable search functionality
    search_fields: Tuple[str] = ('code',)
    # Default ordering of records
    ordering: Tuple[str] = ('code',)
    # Unused configurations are removed for clarity
    filter_horizontal: Tuple = ()
    list_filter: Tuple = ()
    fieldsets: Tuple = ()
    add_fieldsets: Tuple = ()

# Admin configuration for the Student_Profile model


@admin.register(Student_Profile)
class StudentProfileAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display: Tuple[str, str, str, str] = (
        'code', 'name', 'email', 'section')
    # Fields to enable search functionality
    search_fields: Tuple[str, str, str] = ('code', 'name', 'section__name')
    # Default ordering of records
    ordering: Tuple[str] = ('code',)

# Admin configuration for the Faculty_Profile model


@admin.register(Faculty_Profile)
class FacultyProfileAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display: Tuple[str, str, str, str] = (
        'code', 'name', 'email', 'department')
    # Fields to enable search functionality
    search_fields: Tuple[str, str, str] = ('code', 'name', 'department__name')
    # Default ordering of records
    ordering: Tuple[str] = ('code',)
