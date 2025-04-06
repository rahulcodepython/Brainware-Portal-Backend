from rest_framework import generics, permissions
from backend.message import Message
from backend.utils import catch_exception
from django.shortcuts import get_object_or_404
from .models import Course, Module, Lecture
from .serializers import CourseSerializer, ModuleSerializer, LectureSerializer


# Generic View for creating a course
class CreateCourse(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def create(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        if not serialized.is_valid():
            return Message.error(serialized.errors)
        serialized.save()
        return Message.success("Course created successfully.")


# Generic View for listing all courses
class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def list(self, request, *args, **kwargs):
        serialized = self.get_serializer(self.get_queryset(), many=True)
        return Message.success(serialized.data)


# Generic View for retrieving, updating, or deleting a specific course
class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized = self.get_serializer(instance)
        return Message.success(serialized.data)

    @catch_exception
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized = self.get_serializer(
            instance, data=request.data, partial=True)
        if not serialized.is_valid():
            return Message.error(serialized.errors)
        serialized.save()
        return Message.success("Course updated successfully.")

    @catch_exception
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Message.success("Course deleted successfully.")


# Generic View for creating a module
class CreateModule(generics.CreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def create(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        if not serialized.is_valid():
            return Message.error(serialized.errors)
        serialized.save()
        return Message.success("Module created successfully.")


# Generic View for listing all modules
class ModuleList(generics.ListAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def list(self, request, *args, **kwargs):
        serialized = self.get_serializer(self.get_queryset(), many=True)
        return Message.success(serialized.data)


# Generic View for retrieving, updating, or deleting a specific module
class ModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized = self.get_serializer(instance)
        return Message.success(serialized.data)

    @catch_exception
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized = self.get_serializer(
            instance, data=request.data, partial=True)
        if not serialized.is_valid():
            return Message.error(serialized.errors)
        serialized.save()
        return Message.success("Module updated successfully.")

    @catch_exception
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Message.success("Module deleted successfully.")


# Generic View for creating a lecture
class CreateLecture(generics.CreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def create(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)
        if not serialized.is_valid():
            return Message.error(serialized.errors)
        serialized.save()
        return Message.success("Lecture created successfully.")


# Generic View for listing all lectures
class LectureList(generics.ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def list(self, request, *args, **kwargs):
        serialized = self.get_serializer(self.get_queryset(), many=True)
        return Message.success(serialized.data)


# Generic View for retrieving, updating, or deleting a specific lecture
class LectureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized = self.get_serializer(instance)
        return Message.success(serialized.data)

    @catch_exception
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serialized = self.get_serializer(
            instance, data=request.data, partial=True)
        if not serialized.is_valid():
            return Message.error(serialized.errors)
        serialized.save()
        return Message.success("Lecture updated successfully.")

    @catch_exception
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Message.success("Lecture deleted successfully.")
