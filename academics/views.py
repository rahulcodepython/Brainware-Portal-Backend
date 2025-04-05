from rest_framework import views, permissions
from backend.message import Message
from backend.utils import catch_exception
from .models import Semester
from django.shortcuts import get_object_or_404
from .serializers import (
    DepartmentSerializer,
    BatchSerializer,
    SectionSerializer,
    SemesterSerializer,
)


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


# Creating new Course to Semester api
class AddCourseToSemester(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        semester = get_object_or_404(Semester, id=request.data['semester'])
        request.data.pop('semester')

        serialized = SemesterSerializer(
            semester, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success('Course added to semester successfully')
