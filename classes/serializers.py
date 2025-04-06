from rest_framework import serializers
from .models import Class_Routine, LecturePlan, Attendance
from academics.models import Semester, Section, Semester_Course_Faculty
from courses.models import Course, Module
from authentication.models import Student_Profile
from django.shortcuts import get_object_or_404
from typing import Any, Dict


class ClassRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Routine
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True, "required": False},
        }

    def validate_data(self, validated_data: Dict[str, Any]) -> None:
        # Fetch the section object
        section = get_object_or_404(Section, id=validated_data['section'])

        # Check if the section belongs to the semester
        semester = validated_data["semester"]
        if semester not in section.batch.semesters.all():
            raise serializers.ValidationError(
                "Section does not belong to the semester")

        # Check if the course belongs to the semester
        course_id = validated_data['course'].id
        semester_courses = Semester.objects.filter(
            id=semester).values_list('courses__id', flat=True)
        if course_id not in semester_courses:
            raise serializers.ValidationError(
                "Course does not belong to the semester")

        # Check if the faculty belongs to the course
        faculty_id = validated_data['faculty'].id
        valid_faculties = Semester_Course_Faculty.objects.filter(
            semester=semester, course=validated_data['course']
        ).values_list('faculty__id', flat=True)
        if faculty_id not in valid_faculties:
            raise serializers.ValidationError(
                "Faculty does not belong to the course")

    def create(self, validated_data: Dict[str, Any]) -> Class_Routine:
        # Validate data before creating the object
        self.validate_data(validated_data)
        return super().create(validated_data)

    def update(self, instance: Class_Routine, validated_data: Dict[str, Any]) -> Class_Routine:
        # Validate data before updating the object
        self.validate_data(validated_data)
        return super().update(instance, validated_data)


class AddLecturePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturePlan
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True, "required": False},
        }

    def validate_data(self, validated_data: Dict[str, Any]) -> None:
        # Fetch the section object
        section = get_object_or_404(Section, id=validated_data['section'])

        # Check if the section belongs to the semester
        semester = validated_data["semester"]
        if semester not in section.batch.semesters.all():
            raise serializers.ValidationError(
                "Section does not belong to the semester")

        # Check if the course belongs to the semester
        course_id = validated_data['course'].id
        semester_courses = Semester.objects.filter(
            id=semester).values_list('courses__id', flat=True)
        if course_id not in semester_courses:
            raise serializers.ValidationError(
                "Course does not belong to the semester")

        # Check if the module belongs to the course
        module_id = validated_data['module'].id
        course_modules = Course.objects.filter(
            id=validated_data['course']).values_list('modules__id', flat=True)
        if module_id not in course_modules:
            raise serializers.ValidationError(
                "Module does not belong to the course")

        # Check if the lecture belongs to the module
        lecture_id = validated_data['lecture'].id
        module_lectures = Module.objects.filter(
            id=module_id).values_list('lectures__id', flat=True)
        if lecture_id not in module_lectures:
            raise serializers.ValidationError(
                "Lecture does not belong to the module")

        # Validate lecture plan date matches class routine day
        class_routine = get_object_or_404(
            Class_Routine, id=validated_data['referrence_class_routine'])
        lecture_plan_day = validated_data['assigned_date'].strftime("%A")
        if lecture_plan_day != class_routine.day:
            raise serializers.ValidationError(
                "Lecture plan date does not match with the class routine day")

        # Validate assigned faculties belong to the course
        available_faculties = Semester_Course_Faculty.objects.filter(
            semester=semester, course=validated_data['course']
        ).values_list('faculty', flat=True)
        assigned_faculties = validated_data['assigned_faculties']
        if not all(faculty in available_faculties for faculty in assigned_faculties):
            raise serializers.ValidationError(
                "Assigned faculties do not belong to the course")

    def create(self, validated_data: Dict[str, Any]) -> LecturePlan:
        # Validate data before creating the object
        self.validate_data(validated_data)
        return super().create(validated_data)

    def update(self, instance: LecturePlan, validated_data: Dict[str, Any]) -> LecturePlan:
        # Validate data before updating the object
        self.validate_data(validated_data)
        return super().update(instance, validated_data)


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

    def validate_data(self, validated_data: Dict[str, Any]) -> None:
        # Fetch the lecture plan and student objects
        lecture_plan = get_object_or_404(
            LecturePlan, id=validated_data['lecture_plan'])
        student = get_object_or_404(
            Student_Profile, id=validated_data['student'])

        # Validate attendance date matches lecture plan date
        if validated_data['attendance_date'] != lecture_plan.assigned_date:
            raise serializers.ValidationError(
                "Attendance date does not match with the lecture plan date")

        # Validate student belongs to the section of the lecture plan
        if lecture_plan.section.id != student.section.id:
            raise serializers.ValidationError(
                "Student does not belong to the section of the lecture plan")

    def create(self, validated_data: Dict[str, Any]) -> Attendance:
        # Validate data before creating the object
        self.validate_data(validated_data)
        return super().create(validated_data)
