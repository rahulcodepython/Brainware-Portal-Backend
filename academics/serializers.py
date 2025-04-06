from rest_framework import serializers
from .models import Department, Batch, Section, Semester, Semester_Course_Faculty
from django.shortcuts import get_object_or_404
from courses.models import Course


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


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

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


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

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


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
        if "add_courses" in validated_data:
            add_courses = validated_data.pop("add_courses", [])

            if add_courses:
                courses_to_add = Course.objects.filter(id__in=add_courses)
                instance.courses.add(*courses_to_add)

                for course in courses_to_add:
                    semester_course_faculty = Semester_Course_Faculty.objects.filter(
                        semester=instance, course=course)

                    if not semester_course_faculty.exists():
                        Semester_Course_Faculty.objects.create(
                            semester=instance,
                            course=course,
                            faculty=None
                        )

            validated_data.pop("add_courses", [])

        if "remove_courses" in validated_data:
            remove_courses = validated_data.pop("remove_courses", [])

            if remove_courses:
                courses_to_remove = Course.objects.filter(
                    id__in=remove_courses)
                instance.courses.remove(*courses_to_remove)

                for course in courses_to_remove:
                    semester_course_faculty = Semester_Course_Faculty.objects.filter(
                        semester=instance, course=course)

                    if semester_course_faculty.exists():
                        semester_course_faculty.delete()

            validated_data.pop("remove_courses", [])

        return super().update(instance, validated_data)


class Semester_Course_FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester_Course_Faculty
        fields = '__all__'

    def create(self, validated_data):
        semester_course_faculty = super().create(validated_data)

        semester = semester_course_faculty.semester
        course = semester_course_faculty.course

        if course not in semester.courses.all():
            semester.courses.add(course)

        return semester_course_faculty

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
