from rest_framework import views, permissions
from backend.message import Message
from backend.utils import catch_exception
from .models import (
    Department,
    Batch,
    Section,
    Semester,
    Semester_Course_Faculty,
)
from django.shortcuts import get_object_or_404
from .serializers import (
    DepartmentSerializer,
    BatchSerializer,
    SectionSerializer,
    SemesterSerializer,
    Semester_Course_FacultySerializer,
)
from courses.models import Course


# Creating new Department api
class AddDepartment(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = DepartmentSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success('Department added successfully')


class Departments(views.APIView):
    @catch_exception
    def get(self, request, *args, **kwargs):
        departments = DepartmentSerializer(Department.objects.all(), many=True)
        return Message.success('Departments fetched successfully', departments.data)


class Department(views.APIView):
    @catch_exception
    def get(self, request, *args, **kwargs):
        department = get_object_or_404(Department, id=kwargs['id'])
        serialized = DepartmentSerializer(department)
        return Message.success('Department fetched successfully', serialized.data)

    @catch_exception
    def patch(self, request, *args, **kwargs):
        department = get_object_or_404(Department, id=kwargs['id'])
        serialized = DepartmentSerializer(
            department, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success('Department updated successfully')

    @catch_exception
    def delete(self, request, *args, **kwargs):
        department = get_object_or_404(Department, id=kwargs['id'])
        department.delete()
        return Message.success('Department deleted successfully')


# Creating new Batch api
class AddBatch(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = BatchSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success('Batch added successfully')


class Batches(views.APIView):
    @catch_exception
    def get(self, request, *args, **kwargs):
        batches = BatchSerializer(Batch.objects.all(), many=True)
        return Message.success('Batches fetched successfully', batches.data)


class Batch(views.APIView):
    @catch_exception
    def get(self, request, *args, **kwargs):
        batch = get_object_or_404(Batch, id=kwargs['id'])
        serialized = BatchSerializer(batch)
        return Message.success('Batch fetched successfully', serialized.data)

    @catch_exception
    def patch(self, request, *args, **kwargs):
        batch = get_object_or_404(Batch, id=kwargs['id'])
        serialized = BatchSerializer(
            batch, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success('Batch updated successfully')

    @catch_exception
    def delete(self, request, *args, **kwargs):
        batch = get_object_or_404(Batch, id=kwargs['id'])
        batch.delete()
        return Message.success('Batch deleted successfully')


# Creating new Section api
class AddSection(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = SectionSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success('Section added successfully')


class Sections(views.APIView):
    @catch_exception
    def get(self, request, *args, **kwargs):
        sections = SectionSerializer(Section.objects.all(), many=True)
        return Message.success('Sections fetched successfully', sections.data)


class Section(views.APIView):
    @catch_exception
    def get(self, request, *args, **kwargs):
        section = get_object_or_404(Section, id=kwargs['id'])
        serialized = SectionSerializer(section)
        return Message.success('Section fetched successfully', serialized.data)

    @catch_exception
    def patch(self, request, *args, **kwargs):
        section = get_object_or_404(Section, id=kwargs['id'])
        serialized = SectionSerializer(
            section, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success('Section updated successfully')

    @catch_exception
    def delete(self, request, *args, **kwargs):
        section = get_object_or_404(Section, id=kwargs['id'])
        section.delete()
        return Message.success('Section deleted successfully')


# Creating new Semester api
class AddSemester(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = SemesterSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success('Semester added successfully')


class Semesters(views.APIView):
    @catch_exception
    def get(self, request, *args, **kwargs):
        semesters = SemesterSerializer(Semester.objects.all(), many=True)
        return Message.success('Semesters fetched successfully', semesters.data)


class Semester(views.APIView):
    @catch_exception
    def get(self, request, *args, **kwargs):
        semester = get_object_or_404(Semester, id=kwargs['id'])
        serialized = SemesterSerializer(semester)
        return Message.success('Semester fetched successfully', serialized.data)

    @catch_exception
    def patch(self, request, *args, **kwargs):
        semester = get_object_or_404(Semester, id=kwargs['id'])
        serialized = SemesterSerializer(
            semester, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success('Semester updated successfully')

    @catch_exception
    def delete(self, request, *args, **kwargs):
        semester = get_object_or_404(Semester, id=kwargs['id'])
        semester.delete()
        return Message.success('Semester deleted successfully')


class SemesterCourseFaculty(views.APIView):
    @catch_exception
    def get(self, request, *args, **kwargs):
        semester = get_object_or_404(Semester, id=kwargs['semester'])
        course = get_object_or_404(Course, id=kwargs['course'])
        serialized = Semester_Course_FacultySerializer(
            Semester_Course_Faculty.objects.filter(semester=semester, course=course), many=True)
        return Message.success('Semester Course Faculty fetched successfully', serialized.data)

    @catch_exception
    def patch(self, request, *args, **kwargs):
        semester = get_object_or_404(Semester, id=kwargs['semester'])
        course = get_object_or_404(Course, id=kwargs['course'])
        serialized = Semester_Course_FacultySerializer(
            Semester_Course_Faculty.objects.filter(semester=semester, course=course), data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success('Semester Course Faculty updated successfully')

    @catch_exception
    def delete(self, request, *args, **kwargs):
        semester = get_object_or_404(Semester, id=kwargs['semester'])
        course = get_object_or_404(Course, id=kwargs['course'])
        semester_course_faculty = get_object_or_404(
            Semester_Course_Faculty, semester=semester, course=course)
        semester_course_faculty.delete()
        return Message.success('Semester Course Faculty deleted successfully')
