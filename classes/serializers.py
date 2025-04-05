from rest_framework import serializers
from .models import Class_Routine, Lecture_Plan
from academics.models import Semester, Section
from courses.models import Course, Module
from django.shortcuts import get_object_or_404


class ClassRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Routine
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True, "required": False},
        }

    def create(self, validated_data):
        section = get_object_or_404(Section, id=validated_data['section'])
        if validated_data["semester"] not in section.batch.semesters.all():
            raise serializers.ValidationError(
                "Section does not belong to the semester")

        if validated_data['course'].id not in Semester.objects.filter(id=validated_data['semester']).values_list('courses__id', flat=True):
            raise serializers.ValidationError(
                "Course does not belong to the semester")

        return super().create(validated_data)


class AddLecturePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture_Plan
        fields = '__all__'
        extra_kwargs = {
            "id": {"read_only": True, "required": False},
        }

    def create(self, validated_data):
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

        return super().create(validated_data)
