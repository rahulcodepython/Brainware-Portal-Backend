from django.contrib import admin
from .models import (
    Lecture_Plan, Attendance, Class_Routine, Preparatory_Class
)
# Register your models here.


@admin.register(Lecture_Plan)
class LecturePlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'lecture', 'assigned_date')
    search_fields = ('id',)


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'attendance_status')
    search_fields = ('id',)


@admin.register(Class_Routine)
class ClassRoutineAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'faculty')
    search_fields = ('id',)


@admin.register(Preparatory_Class)
class PreparatoryClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'class_routine', 'approved')
    search_fields = ('id',)
