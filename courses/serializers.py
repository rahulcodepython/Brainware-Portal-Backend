from rest_framework import serializers
from typing import Dict, Any
from .models import Course, Module, Lecture


class CourseSerializer(serializers.ModelSerializer):
    """Serializer for the Course model with complete CRUD operations."""

    class Meta:
        model = Course  # Specify the model to serialize
        fields = '__all__'  # Include all model fields
        extra_kwargs = {
            # Make modules optional and read-only
            'modules': {'required': False, 'read_only': True},
        }

    def create(self, validated_data: Dict[str, Any]) -> Course:
        """
        Create a new Course instance.

        Args:
            validated_data: Dictionary of validated course data

        Returns:
            Course: Newly created course instance
        """
        return super().create(validated_data)

    def update(self, instance: Course, validated_data: Dict[str, Any]) -> Course:
        """
        Update an existing Course instance.

        Args:
            instance: Existing course to update
            validated_data: Dictionary of validated update data

        Returns:
            Course: Updated course instance
        """
        return super().update(instance, validated_data)


class ModuleSerializer(serializers.ModelSerializer):
    """Serializer for the Module model with course relationship handling."""

    class Meta:
        model = Module  # Specify the model to serialize
        fields = '__all__'  # Include all model fields
        extra_kwargs = {
            # Make lectures optional and read-only
            'lectures': {'required': False, 'read_only': True},
        }

    def create(self, validated_data: Dict[str, Any]) -> Module:
        """
        Create a new Module instance and associate with its course.

        Args:
            validated_data: Dictionary of validated module data

        Returns:
            Module: Newly created module instance
        """
        # Create module with validated data
        module: Module = super().create(validated_data)

        # Associate the module with its course if available
        course: Course = module.course
        if course:  # Ensure course exists to avoid runtime errors
            course.modules.add(module)
            course.save()

        return module

    def update(self, instance: Module, validated_data: Dict[str, Any]) -> Module:
        """
        Update an existing Module instance.

        Args:
            instance: Existing module to update
            validated_data: Dictionary of validated update data

        Returns:
            Module: Updated module instance
        """
        return super().update(instance, validated_data)


class LectureSerializer(serializers.ModelSerializer):
    """Serializer for the Lecture model with module relationship handling."""

    class Meta:
        model = Lecture  # Specify the model to serialize
        fields = '__all__'  # Include all model fields

    def create(self, validated_data: Dict[str, Any]) -> Lecture:
        """
        Create a new Lecture instance and associate with its module.

        Args:
            validated_data: Dictionary of validated lecture data

        Returns:
            Lecture: Newly created lecture instance
        """
        # Create lecture with validated data
        lecture: Lecture = super().create(validated_data)

        # Associate the lecture with its module if available
        module: Module = lecture.module
        if module:  # Ensure module exists to avoid runtime errors
            module.lectures.add(lecture)
            module.save()

        return lecture

    def update(self, instance: Lecture, validated_data: Dict[str, Any]) -> Lecture:
        """
        Update an existing Lecture instance.

        Args:
            instance: Existing lecture to update
            validated_data: Dictionary of validated update data

        Returns:
            Lecture: Updated lecture instance
        """
        return super().update(instance, validated_data)
