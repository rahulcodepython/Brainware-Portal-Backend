from rest_framework import serializers
from .models import Department, Batch, Section, Semester
from django.shortcuts import get_object_or_404
from courses.models import Course


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
        batch = super().create(validated_data)

        department = get_object_or_404(
            Department, id=validated_data['department'].id)
        department.batches.add(batch)
        department.save()

        return batch


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

    def create(self, validated_data):
        section = super().create(validated_data)

        batch = get_object_or_404(
            Batch, id=validated_data['batch'].id)
        batch.sections.add(section)
        batch.save()

        return section


class SemesterSerializer(serializers.ModelSerializer):
    add_courses = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )
    remove_courses = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )

    class Meta:
        model = Semester
        fields = '__all__'
        extra_fields = ['add_courses', 'remove_courses']
        extra_kwargs = {
            'courses': {'read_only': False, 'required': False}
        }

    def create(self, validated_data):
        semester = super().create(validated_data)

        batch = semester.batch
        batch.semesters.add(semester)
        batch.save()

        return semester

    def update(self, instance, validated_data):
        add_courses = validated_data.pop("add_courses", [])
        remove_courses = validated_data.pop("remove_courses", [])

        if add_courses:
            courses_to_add = Course.objects.filter(id__in=add_courses)
            instance.courses.add(*courses_to_add)

        if remove_courses:
            courses_to_remove = Course.objects.filter(id__in=remove_courses)
            instance.courses.remove(*courses_to_remove)

        return super().update(instance, validated_data)
