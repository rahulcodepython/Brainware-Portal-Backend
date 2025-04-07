from typing import Any, Dict, List, Optional, Union
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
    Response
)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from backend.message import Message
from backend.utils import catch_exception
from .serializers import (
    ClassRoutineSerializer,
    AddLecturePlanSerializer,
    AttendanceSerializer
)
from .models import Class_Routine, LecturePlan
from django.shortcuts import get_object_or_404
from academics.models import Section


class AddClassRoutine(CreateAPIView):
    """API view for creating a new class routine."""
    permission_classes = [IsAdminUser]
    serializer_class = ClassRoutineSerializer

    @catch_exception
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Create a new class routine.

        Args:
            request: The HTTP request object

        Returns:
            Response with success message and id or error details
        """
        serializer = self.get_serializer(data=request.data)

        # Validate the serializer data
        if not serializer.is_valid():
            return Message.error(serializer.errors)

        # Save the serializer data
        serializer.save()

        # Return success message with id
        return Message.success(
            "Class routine added successfully",
            {"id": serializer.data["id"]}
        )


class ClassRoutines(ListAPIView):
    """API view for listing class routines for a section."""
    permission_classes = [IsAdminUser]
    serializer_class = ClassRoutineSerializer

    @catch_exception
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        List all class routines for a specific section.

        Args:
            request: The HTTP request object
            kwargs: URL parameters including section id

        Returns:
            Response with success message and routine list or error details
        """
        # Get section id from URL parameters
        section_id = kwargs.get('section')

        # Get section object or return 404
        section_obj = get_object_or_404(Section, id=section_id)

        # Filter class routines by section and current semester
        queryset = Class_Routine.objects.filter(
            section=section_obj,
            semester=section_obj.batch.current_semester
        )

        # Serialize the queryset
        serializer = self.get_serializer(queryset, many=True)

        # Return success message with data
        return Message.success(
            "Class routines fetched successfully",
            serializer.data
        )


class ClassRoutine(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    """API view for retrieving, updating, and deleting class routines."""
    permission_classes = [IsAdminUser]
    serializer_class = ClassRoutineSerializer
    queryset = Class_Routine.objects.all()

    @catch_exception
    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Retrieve a specific class routine.

        Args:
            request: The HTTP request object
            kwargs: URL parameters including pk

        Returns:
            Response with success message and routine details
        """
        # Get the instance
        instance = self.get_object()

        # Serialize the instance
        serializer = self.get_serializer(instance)

        # Return success message with data
        return Message.success(
            "Class routine fetched successfully",
            serializer.data
        )

    @catch_exception
    def partial_update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Update a specific class routine partially.

        Args:
            request: The HTTP request object
            kwargs: URL parameters including pk

        Returns:
            Response with success message and updated data or error details
        """
        # Get the instance
        instance = self.get_object()

        # Create serializer with partial update
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)

        # Validate the serializer data
        if not serializer.is_valid():
            return Message.error(serializer.errors)

        # Save the serializer data
        serializer.save()

        # Return success message with updated data
        return Message.success(
            "Class routine updated successfully",
            serializer.data
        )

    @catch_exception
    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Delete a specific class routine.

        Args:
            request: The HTTP request object
            kwargs: URL parameters including pk

        Returns:
            Response with success message
        """
        # Get the instance
        instance = self.get_object()

        # Delete the instance
        instance.delete()

        # Return success message
        return Message.success("Class routine deleted successfully")


class AddLecturePlan(CreateAPIView):
    """API view for creating a new lecture plan."""
    permission_classes = [IsAdminUser]
    serializer_class = AddLecturePlanSerializer

    @catch_exception
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Create a new lecture plan.

        Args:
            request: The HTTP request object

        Returns:
            Response with success message or error details
        """
        # Create serializer with request data
        serializer = self.get_serializer(data=request.data)

        # Validate the serializer data
        if not serializer.is_valid():
            return Message.error(serializer.errors)

        # Save the serializer data
        serializer.save()

        # Return success message
        return Message.success("Lecture plan added successfully")


class LecturePlans(ListAPIView):
    """API view for listing lecture plans for a section and course."""
    permission_classes = [IsAdminUser]
    serializer_class = AddLecturePlanSerializer

    @catch_exception
    def list(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        List all lecture plans for a specific section and course.

        Args:
            request: The HTTP request object
            kwargs: URL parameters including section and course ids

        Returns:
            Response with success message and plans list or error details
        """
        # Get section and course ids from URL parameters
        section_id = kwargs.get('section')
        course_id = kwargs.get('course')

        # Get section object or return 404
        section_obj = get_object_or_404(Section, id=section_id)

        # Filter lecture plans by section, course, and current semester
        queryset = LecturePlan.objects.filter(
            section=section_obj,
            cours=course_id,
            semester=section_obj.batch.current_semester
        )

        # Serialize the queryset
        serializer = self.get_serializer(queryset, many=True)

        # Return success message with data
        return Message.success(
            "Lecture plans fetched successfully",
            serializer.data
        )


class LecturePlan(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    """API view for retrieving, updating, and deleting lecture plans."""
    permission_classes = [IsAdminUser]
    serializer_class = AddLecturePlanSerializer
    queryset = LecturePlan.objects.all()

    @catch_exception
    def retrieve(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Retrieve a specific lecture plan.

        Args:
            request: The HTTP request object
            kwargs: URL parameters including pk

        Returns:
            Response with success message and plan details
        """
        # Get the instance
        instance = self.get_object()

        # Serialize the instance
        serializer = self.get_serializer(instance)

        # Return success message with data
        return Message.success(
            "Lecture plan fetched successfully",
            serializer.data
        )

    @catch_exception
    def partial_update(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Update a specific lecture plan partially.

        Args:
            request: The HTTP request object
            kwargs: URL parameters including pk

        Returns:
            Response with success message and updated data or error details
        """
        # Get the instance
        instance = self.get_object()

        # Create serializer with partial update
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)

        # Validate the serializer data
        if not serializer.is_valid():
            return Message.error(serializer.errors)

        # Save the serializer data
        serializer.save()

        # Return success message with updated data
        return Message.success(
            "Lecture plan updated successfully",
            serializer.data
        )

    @catch_exception
    def destroy(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Delete a specific lecture plan.

        Args:
            request: The HTTP request object
            kwargs: URL parameters including pk

        Returns:
            Response with success message
        """
        # Get the instance
        instance = self.get_object()

        # Delete the instance
        instance.delete()

        # Return success message
        return Message.success("Lecture plan deleted successfully")


class RegisterAttendance(CreateAPIView):
    """API view for registering student attendance."""
    permission_classes = [IsAuthenticated]
    serializer_class = AttendanceSerializer

    @catch_exception
    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        Register attendance for students.

        Args:
            request: The HTTP request object

        Returns:
            Response with success message or error details
        """
        # Create serializer with request data
        serializer = self.get_serializer(data=request.data)

        # Validate the serializer data
        if not serializer.is_valid():
            return Message.error(serializer.errors)

        # Save the serializer data
        serializer.save()

        # Return success message
        return Message.success("Attendance registered successfully.")
