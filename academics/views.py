from typing import Any, Dict
from rest_framework import views, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from backend.message import Message
from backend.utils import catch_exception
from .models import Department, Batch, Section, Semester, Semester_Course_Faculty
from django.shortcuts import get_object_or_404
from .serializers import (
    DepartmentSerializer,
    BatchSerializer,
    SectionSerializer,
    SemesterSerializer,
    Semester_Course_FacultySerializer,
)
from courses.models import Course


# Creating new Department API
class AddDepartment(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # Serialize the incoming data
        serialized: DepartmentSerializer = DepartmentSerializer(
            data=request.data)

        # Validate the serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the department
        serialized.save()

        return Message.success("Department added successfully")


class Departments(views.APIView):
    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # Fetch all departments and serialize them
        departments = Department.objects.all()
        serialized = DepartmentSerializer(departments, many=True)
        return Message.success("Departments fetched successfully", serialized.data)


class Department(views.APIView):
    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch a specific department by ID
        department = get_object_or_404(Department, id=kwargs["id"])
        serialized = DepartmentSerializer(department)
        return Message.success("Department fetched successfully", serialized.data)

    @catch_exception
    def patch(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch and update a specific department
        department = get_object_or_404(Department, id=kwargs["id"])
        serialized = DepartmentSerializer(
            department, data=request.data, partial=True)

        # Validate the serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the updated department
        serialized.save()
        return Message.success("Department updated successfully")

    @catch_exception
    def delete(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch and delete a specific department
        department = get_object_or_404(Department, id=kwargs["id"])
        department.delete()
        return Message.success("Department deleted successfully")


# Creating new Batch API
class AddBatch(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # Serialize the incoming data
        serialized: BatchSerializer = BatchSerializer(data=request.data)

        # Validate the serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the batch
        serialized.save()

        return Message.success("Batch added successfully")


class Batches(views.APIView):
    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # Fetch all batches and serialize them
        batches = Batch.objects.all()
        serialized = BatchSerializer(batches, many=True)
        return Message.success("Batches fetched successfully", serialized.data)


class Batch(views.APIView):
    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch a specific batch by ID
        batch = get_object_or_404(Batch, id=kwargs["id"])
        serialized = BatchSerializer(batch)
        return Message.success("Batch fetched successfully", serialized.data)

    @catch_exception
    def patch(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch and update a specific batch
        batch = get_object_or_404(Batch, id=kwargs["id"])
        serialized = BatchSerializer(batch, data=request.data, partial=True)

        # Validate the serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the updated batch
        serialized.save()
        return Message.success("Batch updated successfully")

    @catch_exception
    def delete(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch and delete a specific batch
        batch = get_object_or_404(Batch, id=kwargs["id"])
        batch.delete()
        return Message.success("Batch deleted successfully")


# Creating new Section API
class AddSection(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # Serialize the incoming data
        serialized: SectionSerializer = SectionSerializer(data=request.data)

        # Validate the serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the section
        serialized.save()

        return Message.success("Section added successfully")


class Sections(views.APIView):
    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # Fetch all sections and serialize them
        sections = Section.objects.all()
        serialized = SectionSerializer(sections, many=True)
        return Message.success("Sections fetched successfully", serialized.data)


class Section(views.APIView):
    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch a specific section by ID
        section = get_object_or_404(Section, id=kwargs["id"])
        serialized = SectionSerializer(section)
        return Message.success("Section fetched successfully", serialized.data)

    @catch_exception
    def patch(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch and update a specific section
        section = get_object_or_404(Section, id=kwargs["id"])
        serialized = SectionSerializer(
            section, data=request.data, partial=True)

        # Validate the serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the updated section
        serialized.save()
        return Message.success("Section updated successfully")

    @catch_exception
    def delete(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch and delete a specific section
        section = get_object_or_404(Section, id=kwargs["id"])
        section.delete()
        return Message.success("Section deleted successfully")
# Creating new Semester API


class AddSemester(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # Serialize the incoming data
        serialized: SemesterSerializer = SemesterSerializer(data=request.data)

        # Validate the serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the semester
        serialized.save()

        return Message.success("Semester added successfully")


class Semesters(views.APIView):
    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        # Fetch all semesters and serialize them
        semesters = Semester.objects.all()
        serialized = SemesterSerializer(semesters, many=True)
        return Message.success("Semesters fetched successfully", serialized.data)


class Semester(views.APIView):
    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch a specific semester by ID
        semester = get_object_or_404(Semester, id=kwargs["id"])
        serialized = SemesterSerializer(semester)
        return Message.success("Semester fetched successfully", serialized.data)

    @catch_exception
    def patch(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch and update a specific semester
        semester = get_object_or_404(Semester, id=kwargs["id"])
        serialized = SemesterSerializer(
            semester, data=request.data, partial=True)

        # Validate the serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the updated semester
        serialized.save()
        return Message.success("Semester updated successfully")

    @catch_exception
    def delete(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch and delete a specific semester
        semester = get_object_or_404(Semester, id=kwargs["id"])
        semester.delete()
        return Message.success("Semester deleted successfully")


class SemesterCourseFaculty(views.APIView):
    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch semester and course
        semester = get_object_or_404(Semester, id=kwargs["semester"])
        course = get_object_or_404(Course, id=kwargs["course"])

        # Fetch and serialize semester-course-faculty data
        semester_course_faculty = Semester_Course_Faculty.objects.filter(
            semester=semester, course=course
        )
        serialized = Semester_Course_FacultySerializer(
            semester_course_faculty, many=True)
        return Message.success("Semester Course Faculty fetched successfully", serialized.data)

    @catch_exception
    def patch(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch semester and course
        semester = get_object_or_404(Semester, id=kwargs["semester"])
        course = get_object_or_404(Course, id=kwargs["course"])

        # Fetch and update semester-course-faculty data
        semester_course_faculty = Semester_Course_Faculty.objects.filter(
            semester=semester, course=course
        )
        serialized = Semester_Course_FacultySerializer(
            semester_course_faculty, data=request.data, partial=True
        )

        # Validate the serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the updated data
        serialized.save()
        return Message.success("Semester Course Faculty updated successfully")

    @catch_exception
    def delete(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        # Fetch semester and course
        semester = get_object_or_404(Semester, id=kwargs["semester"])
        course = get_object_or_404(Course, id=kwargs["course"])

        # Fetch and delete semester-course-faculty data
        semester_course_faculty = get_object_or_404(
            Semester_Course_Faculty, semester=semester, course=course
        )
        semester_course_faculty.delete()
        return Message.success("Semester Course Faculty deleted successfully")
