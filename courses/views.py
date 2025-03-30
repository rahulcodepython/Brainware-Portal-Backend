from rest_framework import views, permissions
from backend.message import Message
from backend.utils import catch_exception
from django.shortcuts import get_object_or_404
from .models import Course, Module, Lecture


class CreateCourse(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        Course.objects.create(
            id=request.data["id"],
            name=request.data["name"]
        )
        return Message.success("Course created successfully.")


class CreateModule(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, id=request.data["course"])

        Module.objects.create(
            id=request.data["id"],
            name=request.data["name"],
            course=course
        )
        return Message.success("Module created successfully.")


class CreateLecture(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        module = get_object_or_404(Module, id=request.data["module"])

        Lecture.objects.create(
            id=request.data["id"],
            name=request.data["name"],
            course_outcome=request.data["course_outcome"],
            module=module
        )
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
