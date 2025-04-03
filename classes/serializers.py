from rest_framework import serializers
from .models import Class_Routine, Lecture_Plan
from academics.models import Semester, Semester_Course
from courses.models import Course, Module
from django.shortcuts import get_object_or_404
import datetime


class ClassRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Routine
        fields = '__all__'

    def create(self, validated_data):
        if validated_data['section'] not in Semester.objects.filter(id=validated_data['semester']).values_list('sections', flat=True):
            raise serializers.ValidationError(
                "Section does not belong to the semester")

        if validated_data['course'] not in Semester_Course.objects.filter(id=validated_data['semester']).values_list('courses', flat=True):
            raise serializers.ValidationError(
                "Course does not belong to the semester")

        return super().create(validated_data)


class AddLecturePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture_Plan
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data['section'])
        print(Semester.objects.filter(id=validated_data['semester']).values_list(
            'sections__id', flat=True))

        if validated_data['section'] not in Semester.objects.filter(id=validated_data['semester']).values_list('sections__id', flat=True):
            raise serializers.ValidationError(
                "Section does not belong to the semester")

        # if validated_data['section'] not in Semester.objects.filter(id=validated_data['semester']).values_list('sections', flat=True):
        #     raise serializers.ValidationError(
        #         "Section does not belong to the semester")

        if validated_data['course'] not in Semester_Course.objects.filter(id=validated_data['semester']).values_list('courses', flat=True):
            raise serializers.ValidationError(
                "Course does not belong to the semester")

        if validated_data['module'] not in Course.objects.filter(id=validated_data['course']).values_list('modules', flat=True):
            raise serializers.ValidationError(
                "Module does not belong to the course")

        if validated_data['lecture'] not in Module.objects.filter(id=validated_data['module']).values_list('lectures', flat=True):
            raise serializers.ValidationError(
                "Lecture does not belong to the module")

        class_routine = get_object_or_404(
            Class_Routine, semester=validated_data['semester'], section=validated_data['section'], course=validated_data['course'])
        class_routine_day = class_routine.day.lower()

        lecture_plan_date = datetime.datetime(validated_data['assigned_date'])
        lecture_plan_day = lecture_plan_date.strftime("%A").lower()

        if class_routine_day != lecture_plan_day:
            raise serializers.ValidationError(
                "Lecture plan date does not match with the class routine day")

        return super().create(validated_data)
