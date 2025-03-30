from django.contrib import admin
from .models import (
    Course, Module, Lecture
)

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course')
    search_fields = ('id', 'name')


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'module')
    search_fields = ('id', 'name')
