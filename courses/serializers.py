from rest_framework import serializers
from .models import Course, Module, Lecture


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        extra_kwargs = {
            'modules': {'required': False, 'read_only': True},
        }

    def create(self, validated_data):
        return super().create(validated_data)


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
        extra_kwargs = {
            'lectures': {'required': False, 'read_only': True},
        }

    def create(self, validated_data):
        return super().create(validated_data)


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
