from rest_framework import serializers  # Import serializers from DRF
# Import helper for fetching objects
from django.shortcuts import get_object_or_404
# Import models
from .models import Department, Batch, Section, Semester, Semester_Course_Faculty
from courses.models import Course  # Import Course model


class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer for Department model"""

    class Meta:
        model = Department
        fields = '__all__'

    def create(self, validated_data: dict) -> Department:
        """Create a new Department instance"""
        return super().create(validated_data)

    def update(self, instance: Department, validated_data: dict) -> Department:
        """Update an existing Department instance"""
        return super().update(instance, validated_data)


class BatchSerializer(serializers.ModelSerializer):
    """Serializer for Batch model"""

    class Meta:
        model = Batch
        fields = '__all__'

    def create(self, validated_data: dict) -> Batch:
        """Create a new Batch instance and associate it with a Department"""
        batch: Batch = super().create(validated_data)

        # Fetch the associated department
        department_id: int = validated_data['department'].id
        department: Department = get_object_or_404(
            Department, id=department_id)

        # Add batch to department and save
        department.batches.add(batch)
        department.save()

        return batch

    def update(self, instance: Batch, validated_data: dict) -> Batch:
        """Update an existing Batch instance"""
        return super().update(instance, validated_data)


class SectionSerializer(serializers.ModelSerializer):
    """Serializer for Section model"""

    class Meta:
        model = Section
        fields = '__all__'

    def create(self, validated_data: dict) -> Section:
        """Create a new Section instance and associate it with a Batch"""
        section: Section = super().create(validated_data)

        # Fetch the associated batch
        batch_id: int = validated_data['batch'].id
        batch: Batch = get_object_or_404(Batch, id=batch_id)

        # Add section to batch and save
        batch.sections.add(section)
        batch.save()

        return section

    def update(self, instance: Section, validated_data: dict) -> Section:
        """Update an existing Section instance"""
        return super().update(instance, validated_data)


class SemesterSerializer(serializers.ModelSerializer):
    """Serializer for Semester model"""

    add_courses = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )  # List of course IDs to add
    remove_courses = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )  # List of course IDs to remove

    class Meta:
        model = Semester
        fields = '__all__'
        extra_kwargs = {
            'courses': {'read_only': False, 'required': False}
        }

    def create(self, validated_data: dict) -> Semester:
        """Create a new Semester instance and associate it with a Batch"""
        semester: Semester = super().create(validated_data)

        # Associate semester with its batch
        batch: Batch = semester.batch
        batch.semesters.add(semester)
        batch.save()

        return semester

    def update(self, instance: Semester, validated_data: dict) -> Semester:
        """Update an existing Semester instance, handling course additions/removals"""

        # Handle adding courses
        add_courses: list[str] = validated_data.pop("add_courses", [])
        if add_courses:
            courses_to_add = Course.objects.filter(id__in=add_courses)
            instance.courses.add(*courses_to_add)

            # Ensure Semester_Course_Faculty exists for added courses
            for course in courses_to_add:
                if not Semester_Course_Faculty.objects.filter(semester=instance, course=course).exists():
                    Semester_Course_Faculty.objects.create(
                        semester=instance,
                        course=course,
                        faculty=None
                    )

        # Handle removing courses
        remove_courses: list[str] = validated_data.pop("remove_courses", [])
        if remove_courses:
            courses_to_remove = Course.objects.filter(id__in=remove_courses)
            instance.courses.remove(*courses_to_remove)

            # Remove associated Semester_Course_Faculty entries
            for course in courses_to_remove:
                Semester_Course_Faculty.objects.filter(
                    semester=instance, course=course
                ).delete()

        return super().update(instance, validated_data)


class Semester_Course_FacultySerializer(serializers.ModelSerializer):
    """Serializer for Semester_Course_Faculty model"""

    class Meta:
        model = Semester_Course_Faculty
        fields = '__all__'

    def create(self, validated_data: dict) -> Semester_Course_Faculty:
        """Create a new Semester_Course_Faculty instance and ensure course is added to semester"""
        semester_course_faculty: Semester_Course_Faculty = super().create(validated_data)

        # Ensure the course is associated with the semester
        semester: Semester = semester_course_faculty.semester
        course: Course = semester_course_faculty.course

        if course not in semester.courses.all():
            semester.courses.add(course)

        return semester_course_faculty

    def update(self, instance: Semester_Course_Faculty, validated_data: dict) -> Semester_Course_Faculty:
        """Update an existing Semester_Course_Faculty instance"""
        return super().update(instance, validated_data)
