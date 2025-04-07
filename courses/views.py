from typing import Any, Dict, List, Optional, Union
from rest_framework import generics, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from backend.message import Message
from backend.utils import catch_exception
from .models import Course, Module, Lecture
from .serializers import CourseSerializer, ModuleSerializer, LectureSerializer


class CreateCourse(generics.CreateAPIView):
    """
    API view for creating a new course.
    Only accessible by admin users.
    """
    queryset = Course.objects.all()  # Define the base queryset for courses
    serializer_class = CourseSerializer  # Specify the serializer for course data
    # Restrict access to admin users
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Create a new course using the provided data.

        Args:
            request: HTTP request containing course data

        Returns:
            Response: Success or error message
        """
        serialized = self.get_serializer(
            data=request.data)  # Create serializer with request data
        if not serialized.is_valid():  # Validate the incoming data
            # Return validation errors if any
            return Message.error(serialized.errors)
        serialized.save()  # Save the new course to database
        # Return success message
        return Message.success("Course created successfully.")


class CourseList(generics.ListAPIView):
    """
    API view for listing all courses.
    Only accessible by admin users.
    """
    queryset = Course.objects.all()  # Define the base queryset for all courses
    serializer_class = CourseSerializer  # Specify the serializer for course data
    # Restrict access to admin users
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        List all available courses.

        Args:
            request: HTTP request

        Returns:
            Response: List of all courses
        """
        queryset = self.get_queryset()  # Get filtered queryset
        serialized = self.get_serializer(
            queryset, many=True)  # Serialize multiple objects
        return Message.success(serialized.data)  # Return serialized data


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific course.
    Only accessible by admin users.
    """
    queryset = Course.objects.all()  # Define the base queryset for courses
    serializer_class = CourseSerializer  # Specify the serializer for course data
    # Restrict access to admin users
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Retrieve a specific course by ID.

        Args:
            request: HTTP request
            kwargs: Contains pk (primary key) for lookup

        Returns:
            Response: Course details
        """
        instance = self.get_object()  # Get the course object
        serialized = self.get_serializer(instance)  # Serialize the course data
        return Message.success(serialized.data)  # Return serialized data

    @catch_exception
    def partial_update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Update specific fields of a course.

        Args:
            request: HTTP request with updated data
            kwargs: Contains pk for course lookup

        Returns:
            Response: Success or error message
        """
        instance = self.get_object()  # Get the course object to update
        serialized = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )  # Create serializer with partial update allowed

        if not serialized.is_valid():  # Validate incoming data
            return Message.error(serialized.errors)  # Return validation errors

        serialized.save()  # Save the updated course
        # Return success message
        return Message.success("Course updated successfully.")

    @catch_exception
    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Delete a specific course.

        Args:
            request: HTTP request
            kwargs: Contains pk for course lookup

        Returns:
            Response: Success message after deletion
        """
        instance = self.get_object()  # Get the course to delete
        instance.delete()  # Delete the course
        # Return success message
        return Message.success("Course deleted successfully.")


class CreateModule(generics.CreateAPIView):
    """
    API view for creating a new module.
    Only accessible by admin users.
    """
    queryset = Module.objects.all()  # Define the base queryset for modules
    serializer_class = ModuleSerializer  # Specify the serializer for module data
    # Restrict access to admin users
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Create a new module using the provided data.

        Args:
            request: HTTP request containing module data

        Returns:
            Response: Success or error message
        """
        serialized = self.get_serializer(
            data=request.data)  # Create serializer with request data
        if not serialized.is_valid():  # Validate the incoming data
            # Return validation errors if any
            return Message.error(serialized.errors)

        serialized.save()  # Save the new module to database
        # Return success message
        return Message.success("Module created successfully.")


class ModuleList(generics.ListAPIView):
    """
    API view for listing all modules.
    Only accessible by admin users.
    """
    queryset = Module.objects.all()  # Define the base queryset for all modules
    serializer_class = ModuleSerializer  # Specify the serializer for module data
    # Restrict access to admin users
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        List all available modules.

        Args:
            request: HTTP request

        Returns:
            Response: List of all modules
        """
        queryset = self.get_queryset()  # Get filtered queryset
        serialized = self.get_serializer(
            queryset, many=True)  # Serialize multiple objects
        return Message.success(serialized.data)  # Return serialized data


class ModuleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific module.
    Only accessible by admin users.
    """
    queryset = Module.objects.all()  # Define the base queryset for modules
    serializer_class = ModuleSerializer  # Specify the serializer for module data
    # Restrict access to admin users
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Retrieve a specific module by ID.

        Args:
            request: HTTP request
            kwargs: Contains pk (primary key) for lookup

        Returns:
            Response: Module details
        """
        instance = self.get_object()  # Get the module object
        serialized = self.get_serializer(instance)  # Serialize the module data
        return Message.success(serialized.data)  # Return serialized data

    @catch_exception
    def partial_update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Update specific fields of a module.

        Args:
            request: HTTP request with updated data
            kwargs: Contains pk for module lookup

        Returns:
            Response: Success or error message
        """
        instance = self.get_object()  # Get the module object to update
        serialized = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )  # Create serializer with partial update allowed

        if not serialized.is_valid():  # Validate incoming data
            return Message.error(serialized.errors)  # Return validation errors

        serialized.save()  # Save the updated module
        # Return success message
        return Message.success("Module updated successfully.")

    @catch_exception
    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Delete a specific module.

        Args:
            request: HTTP request
            kwargs: Contains pk for module lookup

        Returns:
            Response: Success message after deletion
        """
        instance = self.get_object()  # Get the module to delete
        instance.delete()  # Delete the module
        # Return success message
        return Message.success("Module deleted successfully.")


class CreateLecture(generics.CreateAPIView):
    """
    API view for creating a new lecture.
    Only accessible by admin users.
    """
    queryset = Lecture.objects.all()  # Define the base queryset for lectures
    serializer_class = LectureSerializer  # Specify the serializer for lecture data
    # Restrict access to admin users
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Create a new lecture using the provided data.

        Args:
            request: HTTP request containing lecture data

        Returns:
            Response: Success or error message
        """
        serialized = self.get_serializer(
            data=request.data)  # Create serializer with request data
        if not serialized.is_valid():  # Validate the incoming data
            # Return validation errors if any
            return Message.error(serialized.errors)

        serialized.save()  # Save the new lecture to database
        # Return success message
        return Message.success("Lecture created successfully.")


class LectureList(generics.ListAPIView):
    """
    API view for listing all lectures.
    Only accessible by admin users.
    """
    queryset = Lecture.objects.all()  # Define the base queryset for all lectures
    serializer_class = LectureSerializer  # Specify the serializer for lecture data
    # Restrict access to admin users
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        List all available lectures.

        Args:
            request: HTTP request

        Returns:
            Response: List of all lectures
        """
        queryset = self.get_queryset()  # Get filtered queryset
        serialized = self.get_serializer(
            queryset, many=True)  # Serialize multiple objects
        return Message.success(serialized.data)  # Return serialized data


class LectureDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting a specific lecture.
    Only accessible by admin users.
    """
    queryset = Lecture.objects.all()  # Define the base queryset for lectures
    serializer_class = LectureSerializer  # Specify the serializer for lecture data
    # Restrict access to admin users
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Retrieve a specific lecture by ID.

        Args:
            request: HTTP request
            kwargs: Contains pk (primary key) for lookup

        Returns:
            Response: Lecture details
        """
        instance = self.get_object()  # Get the lecture object
        serialized = self.get_serializer(
            instance)  # Serialize the lecture data
        return Message.success(serialized.data)  # Return serialized data

    @catch_exception
    def partial_update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Update specific fields of a lecture.

        Args:
            request: HTTP request with updated data
            kwargs: Contains pk for lecture lookup

        Returns:
            Response: Success or error message
        """
        instance = self.get_object()  # Get the lecture object to update
        serialized = self.get_serializer(
            instance,
            data=request.data,
            partial=True
        )  # Create serializer with partial update allowed

        if not serialized.is_valid():  # Validate incoming data
            return Message.error(serialized.errors)  # Return validation errors

        serialized.save()  # Save the updated lecture
        # Return success message
        return Message.success("Lecture updated successfully.")

    @catch_exception
    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Delete a specific lecture.

        Args:
            request: HTTP request
            kwargs: Contains pk for lecture lookup

        Returns:
            Response: Success message after deletion
        """
        instance = self.get_object()  # Get the lecture to delete
        instance.delete()  # Delete the lecture
        # Return success message
        return Message.success("Lecture deleted successfully.")
