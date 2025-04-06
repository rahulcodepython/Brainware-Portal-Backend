from rest_framework import serializers
from .models import Class_Routine, Lecture_Plan, Attendance
from academics.models import Semester, Section, Semester_Course_Faculty
from courses.models import Course, Module
from authentication.models import Student_Profile
from django.shortcuts import get_object_or_404


class ClassRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Routine
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True, "required": False},
        }

    def validate_data(self, validated_data):
        section = get_object_or_404(Section, id=validated_data['section'])
        if validated_data["semester"] not in section.batch.semesters.all():
            raise serializers.ValidationError(
                "Section does not belong to the semester")

        if validated_data['course'].id not in Semester.objects.filter(id=validated_data['semester']).values_list('courses__id', flat=True):
            raise serializers.ValidationError(
                "Course does not belong to the semester")

        if validated_data['faculty'].id not in Semester_Course_Faculty.objects.filter(semester=validated_data['semester'], course=validated_data['course']).values_list('faculty__id', flat=True):
            raise serializers.ValidationError(
                "Faculty does not belong to the course")

    def create(self, validated_data):
        self.validate_data(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.validate_data(validated_data)
        return super().update(instance, validated_data)


class AddLecturePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture_Plan
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True, "required": False},
        }

    def validate_data(self, validated_data):
        section = get_object_or_404(Section, id=validated_data['section'])
        if validated_data["semester"] not in section.batch.semesters.all():
            raise serializers.ValidationError(
                "Section does not belong to the semester")

        if validated_data['course'].id not in Semester.objects.filter(id=validated_data['semester']).values_list('courses__id', flat=True):
            raise serializers.ValidationError(
                "Course does not belong to the semester")

        if validated_data['module'].id not in Course.objects.filter(id=validated_data['course']).values_list('modules__id', flat=True):
            raise serializers.ValidationError(
                "Module does not belong to the course")

        if validated_data['lecture'].id not in Module.objects.filter(id=validated_data['module']).values_list('lectures__id', flat=True):
            raise serializers.ValidationError(
                "Lecture does not belong to the module")

        class_routine_day = Class_Routine.objects.get(
            id=validated_data['referrence_class_routine'])
        lecture_plan_day = validated_data['assigned_date'].strftime("%A")

        if lecture_plan_day != class_routine_day.day:
            raise serializers.ValidationError(
                "Lecture plan date does not match with the class routine day")

        available_faculty = Semester_Course_Faculty.objects.filter(
            semester=validated_data['semester'], course=validated_data['course']).values_list('faculty', flat=True)
        assigned_faculty = validated_data['assigned_faculties']

        if not all(faculty in available_faculty for faculty in assigned_faculty):
            raise serializers.ValidationError(
                "Assigned faculties do not belong to the course")

    def create(self, validated_data):
        self.validate_data(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.validate_data(validated_data)
        return super().update(instance, validated_data)


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

    def validate_data(self, validate_data):
        lecture_plan = get_object_or_404(
            Lecture_Plan, id=validate_data['lecture_plan'])
        student = get_object_or_404(
            Student_Profile, id=validate_data['student'])

        if validate_data['attendance_date'] != lecture_plan.assigned_date:
            raise serializers.ValidationError(
                "Attendance date does not match with the lecture plan date")

        if lecture_plan.section.id != student.section.id:
            raise serializers.ValidationError(
                "Student does not belong to the section of the lecture plan")

    def create(self, validated_data):
        self.validate_data(validated_data)
        return super().create(validated_data)
