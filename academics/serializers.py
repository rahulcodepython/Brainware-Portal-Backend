from rest_framework import serializers
from .models import Department, Batch, Section, Semester


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)


class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
