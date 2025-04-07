from rest_framework import serializers
from typing import Any, Dict, List, Set
from django.shortcuts import get_object_or_404
from django.db.models import QuerySet

from .models import Class_Routine, LecturePlan, Attendance
from academics.models import Semester, Section, Semester_Course_Faculty
from courses.models import Course, Module
from authentication.models import Student_Profile


class ClassRoutineSerializer(serializers.ModelSerializer):
    """
    Serializer for Class_Routine model with custom validation logic.
    Ensures section belongs to semester, course belongs to semester,
    and faculty belongs to the course.
    """

    class Meta:
        model = Class_Routine
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True, "required": False},
        }

    def validate_data(self, validated_data: Dict[str, Any]) -> None:
        """
        Validates that all relationships between section, semester, course and faculty are valid.

        Args:
            validated_data: Dictionary containing the data to validate

        Raises:
            ValidationError: If any validation fails
        """
        # Fetch the section object
        section: Section = get_object_or_404(
            Section, id=validated_data['section'])

        # Get the semester from validated data
        semester: Semester = validated_data["semester"]

        # Check if the section belongs to the semester
        if semester not in section.batch.semesters.all():
            raise serializers.ValidationError(
                "Section does not belong to the semester")

        # Get the course ID
        course_id: int = validated_data['course'].id

        # Get all courses for this semester
        semester_courses: QuerySet = Semester.objects.filter(
            id=semester).values_list('courses__id', flat=True)

        # Check if course belongs to semester
        if course_id not in semester_courses:
            raise serializers.ValidationError(
                "Course does not belong to the semester")

        # Get faculty ID
        faculty_id: int = validated_data['faculty'].id

        # Get all valid faculties for this course in this semester
        valid_faculties: QuerySet = Semester_Course_Faculty.objects.filter(
            semester=semester, course=validated_data['course']
        ).values_list('faculty__id', flat=True)

        # Check if faculty is valid for this course
        if faculty_id not in valid_faculties:
            raise serializers.ValidationError(
                "Faculty does not belong to the course")

    def create(self, validated_data: Dict[str, Any]) -> Class_Routine:
        """
        Creates a new Class_Routine instance after validating the data.

        Args:
            validated_data: Dictionary containing the data to create the instance

        Returns:
            The created Class_Routine instance
        """
        # Validate data before creating the object
        self.validate_data(validated_data)
        return super().create(validated_data)

    def update(self, instance: Class_Routine, validated_data: Dict[str, Any]) -> Class_Routine:
        """
        Updates an existing Class_Routine instance after validating the data.

        Args:
            instance: The existing Class_Routine instance
            validated_data: Dictionary containing the data to update the instance

        Returns:
            The updated Class_Routine instance
        """
        # Validate data before updating the object
        self.validate_data(validated_data)
        return super().update(instance, validated_data)


class AddLecturePlanSerializer(serializers.ModelSerializer):
    """
    Serializer for LecturePlan model with custom validation logic.
    Ensures section belongs to semester, course belongs to semester,
    module belongs to course, lecture belongs to module, and more.
    """

    class Meta:
        model = LecturePlan
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True, "required": False},
        }

    def validate_data(self, validated_data: Dict[str, Any]) -> None:
        """
        Validates complex relationships between entities in the lecture plan.

        Args:
            validated_data: Dictionary containing the data to validate

        Raises:
            ValidationError: If any validation fails
        """
        # Fetch the section object
        section: Section = get_object_or_404(
            Section, id=validated_data['section'])

        # Get the semester from validated data
        semester: Semester = validated_data["semester"]

        # Check if the section belongs to the semester
        if semester not in section.batch.semesters.all():
            raise serializers.ValidationError(
                "Section does not belong to the semester")

        # Get the course ID
        course_id: int = validated_data['course'].id

        # Get all courses for this semester
        semester_courses: QuerySet = Semester.objects.filter(
            id=semester).values_list('courses__id', flat=True)

        # Check if course belongs to semester
        if course_id not in semester_courses:
            raise serializers.ValidationError(
                "Course does not belong to the semester")

        # Get module ID
        module_id: int = validated_data['module'].id

        # Get all modules for this course
        course_modules: QuerySet = Course.objects.filter(
            id=validated_data['course'].id).values_list('modules__id', flat=True)

        # Check if module belongs to course
        if module_id not in course_modules:
            raise serializers.ValidationError(
                "Module does not belong to the course")

        # Get lecture ID
        lecture_id: int = validated_data['lecture'].id

        # Get all lectures for this module
        module_lectures: QuerySet = Module.objects.filter(
            id=module_id).values_list('lectures__id', flat=True)

        # Check if lecture belongs to module
        if lecture_id not in module_lectures:
            raise serializers.ValidationError(
                "Lecture does not belong to the module")

        # Get class routine
        class_routine: Class_Routine = get_object_or_404(
            Class_Routine, id=validated_data['referrence_class_routine'])

        # Get day of week from lecture plan date
        lecture_plan_day: str = validated_data['assigned_date'].strftime("%A")

        # Check if day matches class routine day
        if lecture_plan_day != class_routine.day:
            raise serializers.ValidationError(
                "Lecture plan date does not match with the class routine day")

        # Get available faculties for this course in this semester
        available_faculties: QuerySet = Semester_Course_Faculty.objects.filter(
            semester=semester, course=validated_data['course']
        ).values_list('faculty', flat=True)

        # Get assigned faculties
        assigned_faculties: List = validated_data['assigned_faculties']

        # Check if all assigned faculties are available for this course
        if not all(faculty in available_faculties for faculty in assigned_faculties):
            raise serializers.ValidationError(
                "Assigned faculties do not belong to the course")

    def create(self, validated_data: Dict[str, Any]) -> LecturePlan:
        """
        Creates a new LecturePlan instance after validating the data.

        Args:
            validated_data: Dictionary containing the data to create the instance

        Returns:
            The created LecturePlan instance
        """
        # Validate data before creating the object
        self.validate_data(validated_data)
        return super().create(validated_data)

    def update(self, instance: LecturePlan, validated_data: Dict[str, Any]) -> LecturePlan:
        """
        Updates an existing LecturePlan instance after validating the data.

        Args:
            instance: The existing LecturePlan instance
            validated_data: Dictionary containing the data to update the instance

        Returns:
            The updated LecturePlan instance
        """
        # Validate data before updating the object
        self.validate_data(validated_data)
        return super().update(instance, validated_data)


class AttendanceSerializer(serializers.ModelSerializer):
    """
    Serializer for Attendance model with custom validation logic.
    Ensures attendance date matches lecture plan date and student belongs to the section.
    """

    class Meta:
        model = Attendance
        fields = '__all__'

    def validate_data(self, validated_data: Dict[str, Any]) -> None:
        """
        Validates attendance data including date matching and student section.

        Args:
            validated_data: Dictionary containing the data to validate

        Raises:
            ValidationError: If any validation fails
        """
        # Fetch the lecture plan and student objects
        lecture_plan: LecturePlan = get_object_or_404(
            LecturePlan, id=validated_data['lecture_plan'])
        student: Student_Profile = get_object_or_404(
            Student_Profile, id=validated_data['student'])

        # Check if attendance date matches lecture plan date
        if validated_data['attendance_date'] != lecture_plan.assigned_date:
            raise serializers.ValidationError(
                "Attendance date does not match with the lecture plan date")

        # Check if student belongs to the section of the lecture plan
        if lecture_plan.section.id != student.section.id:
            raise serializers.ValidationError(
                "Student does not belong to the section of the lecture plan")

    def create(self, validated_data: Dict[str, Any]) -> Attendance:
        """
        Creates a new Attendance instance after validating the data.

        Args:
            validated_data: Dictionary containing the data to create the instance

        Returns:
            The created Attendance instance
        """
        # Validate data before creating the object
        self.validate_data(validated_data)
        return super().create(validated_data)
