from rest_framework import serializers  # Importing serializers from DRF
from .models import Course, Module, Lecture  # Importing models

# Serializer for the Course model


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course  # Specify the model
        fields = '__all__'  # Include all fields in the serializer
        extra_kwargs = {
            # Make 'modules' optional and read-only
            'modules': {'required': False, 'read_only': True},
        }

    def create(self, validated_data: dict) -> Course:
        # Create a new Course instance
        return super().create(validated_data)

    def update(self, instance: Course, validated_data: dict) -> Course:
        # Update an existing Course instance
        return super().update(instance, validated_data)


# Serializer for the Module model
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module  # Specify the model
        fields = '__all__'  # Include all fields in the serializer
        extra_kwargs = {
            # Make 'lectures' optional and read-only
            'lectures': {'required': False, 'read_only': True},
        }

    def create(self, validated_data: dict) -> Module:
        # Create a new Module instance
        module = super().create(validated_data)

        # Associate the module with its course
        course = module.course
        if course:  # Ensure course exists to avoid runtime errors
            course.modules.add(module)
            course.save()

        return module

    def update(self, instance: Module, validated_data: dict) -> Module:
        # Update an existing Module instance
        return super().update(instance, validated_data)


# Serializer for the Lecture model
class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture  # Specify the model
        fields = '__all__'  # Include all fields in the serializer

    def create(self, validated_data: dict) -> Lecture:
        # Create a new Lecture instance
        lecture = super().create(validated_data)

        # Associate the lecture with its module
        module = lecture.module
        if module:  # Ensure module exists to avoid runtime errors
            module.lectures.add(lecture)
            module.save()

        return lecture

    def update(self, instance: Lecture, validated_data: dict) -> Lecture:
        # Update an existing Lecture instance
        return super().update(instance, validated_data)
