from typing import Any, Dict
from rest_framework import generics, permissions
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


# Department Views
class AddDepartment(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response = super().post(request, *args, **kwargs)
        if response.status_code == 201:
            return Message.success("Department added successfully")
        return response


class Departments(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response = super().get(request, *args, **kwargs)
        return Message.success("Departments fetched successfully", response.data)


class Department(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().get(request, *args, **kwargs)
        return Message.success("Department fetched successfully", response.data)

    @catch_exception
    def patch(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().patch(request, *args, **kwargs)
        if response.status_code == 200:
            return Message.success("Department updated successfully")
        return response

    @catch_exception
    def delete(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            return Message.success("Department deleted successfully")
        return response


# Batch Views
class AddBatch(generics.CreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response = super().post(request, *args, **kwargs)
        if response.status_code == 201:
            return Message.success("Batch added successfully")
        return response


class Batches(generics.ListAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response = super().get(request, *args, **kwargs)
        return Message.success("Batches fetched successfully", response.data)


class Batch(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().get(request, *args, **kwargs)
        return Message.success("Batch fetched successfully", response.data)

    @catch_exception
    def patch(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().patch(request, *args, **kwargs)
        if response.status_code == 200:
            return Message.success("Batch updated successfully")
        return response

    @catch_exception
    def delete(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            return Message.success("Batch deleted successfully")
        return response


# Section Views
class AddSection(generics.CreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response = super().post(request, *args, **kwargs)
        if response.status_code == 201:
            return Message.success("Section added successfully")
        return response


class Sections(generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response = super().get(request, *args, **kwargs)
        return Message.success("Sections fetched successfully", response.data)


class Section(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().get(request, *args, **kwargs)
        return Message.success("Section fetched successfully", response.data)

    @catch_exception
    def patch(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().patch(request, *args, **kwargs)
        if response.status_code == 200:
            return Message.success("Section updated successfully")
        return response

    @catch_exception
    def delete(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            return Message.success("Section deleted successfully")
        return response


# Semester Views
class AddSemester(generics.CreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response = super().post(request, *args, **kwargs)
        if response.status_code == 201:
            return Message.success("Semester added successfully")
        return response


class Semesters(generics.ListAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        response = super().get(request, *args, **kwargs)
        return Message.success("Semesters fetched successfully", response.data)


class Semester(generics.RetrieveUpdateDestroyAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().get(request, *args, **kwargs)
        return Message.success("Semester fetched successfully", response.data)

    @catch_exception
    def patch(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().patch(request, *args, **kwargs)
        if response.status_code == 200:
            return Message.success("Semester updated successfully")
        return response

    @catch_exception
    def delete(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            return Message.success("Semester deleted successfully")
        return response


# SemesterCourseFaculty Views
class SemesterCourseFaculty(generics.GenericAPIView):
    serializer_class = Semester_Course_FacultySerializer

    @catch_exception
    def get(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        semester = get_object_or_404(Semester, id=kwargs["semester"])
        course = get_object_or_404(Course, id=kwargs["course"])
        semester_course_faculty = Semester_Course_Faculty.objects.filter(
            semester=semester, course=course
        )
        serialized = self.get_serializer(semester_course_faculty, many=True)
        return Message.success("Semester Course Faculty fetched successfully", serialized.data)

    @catch_exception
    def patch(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        semester = get_object_or_404(Semester, id=kwargs["semester"])
        course = get_object_or_404(Course, id=kwargs["course"])
        semester_course_faculty = Semester_Course_Faculty.objects.filter(
            semester=semester, course=course
        )
        serialized = self.get_serializer(
            semester_course_faculty, data=request.data, partial=True, many=True
        )
        if not serialized.is_valid():
            return Message.error(serialized.errors)
        serialized.save()
        return Message.success("Semester Course Faculty updated successfully")

    @catch_exception
    def delete(self, request: Request, *args: Any, **kwargs: Dict[str, int]) -> Response:
        semester = get_object_or_404(Semester, id=kwargs["semester"])
        course = get_object_or_404(Course, id=kwargs["course"])
        semester_course_faculty = get_object_or_404(
            Semester_Course_Faculty, semester=semester, course=course
        )
        semester_course_faculty.delete()
        return Message.success("Semester Course Faculty deleted successfully")
