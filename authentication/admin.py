from .models import (
    User, Student_Profile, Faculty_Profile
)
from django.contrib.auth.models import Group as DjangoGroup
from django.contrib import admin

# Register your models here.

admin.site.site_header = 'Brainware University'
admin.site.site_title = 'Brainware University'

admin.site.unregister(DjangoGroup)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('code', 'is_superuser', 'is_active', 'is_staff')
    search_fields = ('code',)
    ordering = ('code',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = ()


@admin.register(Student_Profile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'email', 'section')
    search_fields = ('code', 'name', 'section__name')
    ordering = ('code',)


@admin.register(Faculty_Profile)
class FacultyProfileAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'email', 'department')
    search_fields = ('code', 'name', 'department__name')
    ordering = ('code',)
