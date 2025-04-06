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


class CourseList(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        serialized = CourseSerializer(courses, many=True)

        return Message.success(serialized.data)


class CourseDetail(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, id, *args, **kwargs):
        course = get_object_or_404(Course, id=id)
        serialized = CourseSerializer(course)

        return Message.success(serialized.data)

    @catch_exception
    def patch(self, request, id, *args, **kwargs):
        course = get_object_or_404(Course, id=id)
        serialized = CourseSerializer(course, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success("Course updated successfully.")

    @catch_exception
    def delete(self, request, id, *args, **kwargs):
        course = get_object_or_404(Course, id=id)
        course.delete()

        return Message.success("Course deleted successfully.")


class CreateModule(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = ModuleSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success("Module created successfully.")


class ModuleList(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, *args, **kwargs):
        modules = Module.objects.all()
        serialized = ModuleSerializer(modules, many=True)

        return Message.success(serialized.data)


class ModuleDetail(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, id, *args, **kwargs):
        module = get_object_or_404(Module, id=id)
        serialized = ModuleSerializer(module)

        return Message.success(serialized.data)

    @catch_exception
    def patch(self, request, id, *args, **kwargs):
        module = get_object_or_404(Module, id=id)
        serialized = ModuleSerializer(module, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success("Module updated successfully.")

    @catch_exception
    def delete(self, request, id, *args, **kwargs):
        module = get_object_or_404(Module, id=id)
        module.delete()

        return Message.success("Module deleted successfully.")


class CreateLecture(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = LectureSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success("Lecture created successfully.")


class LectureList(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, *args, **kwargs):
        lectures = Lecture.objects.all()
        serialized = LectureSerializer(lectures, many=True)

        return Message.success(serialized.data)


class LectureDetail(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, id, *args, **kwargs):
        lecture = get_object_or_404(Lecture, id=id)
        serialized = LectureSerializer(lecture)

        return Message.success(serialized.data)

    @catch_exception
    def patch(self, request, id, *args, **kwargs):
        lecture = get_object_or_404(Lecture, id=id)
        serialized = LectureSerializer(
            lecture, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success("Lecture updated successfully.")

    @catch_exception
    def delete(self, request, id, *args, **kwargs):
        lecture = get_object_or_404(Lecture, id=id)
        lecture.delete()

        return Message.success("Lecture deleted successfully.")
