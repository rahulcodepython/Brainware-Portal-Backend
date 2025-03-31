from rest_framework import views, permissions
from backend.message import Message
from backend.utils import catch_exception
from django.shortcuts import get_object_or_404
from .models import Course, Module, Lecture
from .serializers import CourseSerializer, ModuleSerializer, LectureSerializer


class CreateCourse(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = CourseSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success("Course created successfully.")


class CreateModule(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = ModuleSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success("Module created successfully.")


class CreateLecture(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = LectureSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success("Lecture created successfully.")


class AddModuleToCourse(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=request.data["course"])
        module = get_object_or_404(Module, id=request.data["module"])

        course.modules.add(module)
        return Message.success("Module added to course successfully.")


class AddLectureToModule(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        module = get_object_or_404(Module, id=request.data["module"])
        lecture = get_object_or_404(Lecture, id=request.data["lecture"])

        module.lectures.add(lecture)
        return Message.success("Lecture added to module successfully.")
