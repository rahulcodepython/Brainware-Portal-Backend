from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from typing import Dict, Any, Optional

from backend.message import Message
from backend.utils import catch_exception
from .serializers import (
    LoginSerializer,
    UserSerializer,
    Student_ProfileSerializer,
    Faculty_ProfileSerializer,
)
from .models import Student_Profile, Faculty_Profile, User


class Login(generics.GenericAPIView):
    """
    View for handling user authentication and token generation.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    @catch_exception
    def post(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Authenticate user and return JWT tokens if credentials are valid.
        
        Args:
            request: HTTP request object containing login credentials
            
        Returns:
            Response: Success response with tokens or error message
        """
        # Validate the incoming data
        serialized = self.get_serializer(data=request.data)
        
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Extract credentials
        username: str = serialized.validated_data["code"]
        password: str = serialized.validated_data["password"]
        
        # Authenticate the user
        user: Optional[User] = authenticate(username=username, password=password)

        if user is None:
            return Message.error('Invalid credentials.')

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token: str = str(refresh.access_token)
        refresh_token: str = str(refresh)
        
        # Return success response with tokens
        return Message.success('Login successful', {"refresh": refresh_token, "access": access_token})


class AddStudent(generics.CreateAPIView):
    """
    View for adding new student users by admins.
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer

    @catch_exception
    def post(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Create a new student user and profile.
        
        Args:
            request: HTTP request object containing user and profile data
            
        Returns:
            Response: Success or error message
        """
        # Validate and create user
        serialized_user = self.get_serializer(data=request.data)
        
        if not serialized_user.is_valid():
            return Message.error(serialized_user.errors)

        user: User = serialized_user.save()

        # Validate and create student profile
        serialized_student = Student_ProfileSerializer(data=request.data)
        
        if not serialized_student.is_valid():
            user.delete()  # Rollback user creation if profile is invalid
            return Message.error(serialized_student.errors)

        serialized_student.save(user=user)
        
        return Message.success('Student added successfully')


class StudentList(generics.ListAPIView):
    """
    View for listing all student profiles for admin users.
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = Student_Profile.objects.all()
    serializer_class = Student_ProfileSerializer

    @catch_exception
    def get(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Get list of all student profiles.
        
        Returns:
            Response: List of student profiles with success message
        """
        students = self.get_queryset()
        serialized_students = self.get_serializer(students, many=True).data
        
        return Message.success('Students retrieved successfully', serialized_students)


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting student profiles.
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = Student_Profile.objects.all()
    serializer_class = Student_ProfileSerializer
    lookup_field = 'code'

    @catch_exception
    def get(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Get a specific student profile.
        
        Args:
            kwargs: Contains code parameter for lookup
            
        Returns:
            Response: Student profile data with success message
        """
        student = self.get_object()
        serialized_student = self.get_serializer(student).data
        
        return Message.success('Student retrieved successfully', serialized_student)

    @catch_exception
    def patch(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Update a student user and profile.
        
        Args:
            request: HTTP request with update data
            kwargs: Contains code parameter for lookup
            
        Returns:
            Response: Success or error message
        """
        # Get and update user data
        code: str = kwargs['code']
        user: User = get_object_or_404(User, code=code)
        serialized_user = UserSerializer(user, data=request.data, partial=True)
        
        if not serialized_user.is_valid():
            return Message.error(serialized_user.errors)

        serialized_user.save()

        # Get and update student profile data
        student = self.get_object()
        serialized_student = self.get_serializer(
            student, data=request.data, partial=True)
        
        if not serialized_student.is_valid():
            return Message.error(serialized_student.errors)

        serialized_student.save()
        
        return Message.success('Student updated successfully')

    @catch_exception
    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Delete a student user and profile.
        
        Args:
            kwargs: Contains code parameter for lookup
            
        Returns:
            Response: Success message
        """
        code: str = kwargs['code']
        user: User = get_object_or_404(User, code=code)
        user.delete()  # Cascade delete will remove the profile as well
        
        return Message.success('Student deleted successfully')


class AddFaculty(generics.CreateAPIView):
    """
    View for adding new faculty users by admins.
    """
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer

    @catch_exception
    def post(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Create a new faculty user and profile.
        
        Args:
            request: HTTP request object containing user and profile data
            
        Returns:
            Response: Success or error message
        """
        # Validate and create user
        serialized_user = self.get_serializer(data=request.data)
        
        if not serialized_user.is_valid():
            return Message.error(serialized_user.errors)

        user: User = serialized_user.save()

        # Validate and create faculty profile
        serialized_faculty = Faculty_ProfileSerializer(data=request.data)
        
        if not serialized_faculty.is_valid():
            user.delete()  # Rollback user creation if profile is invalid
            return Message.error(serialized_faculty.errors)

        serialized_faculty.save(user=user)
        
        return Message.success('Faculty added successfully')


class FacultyList(generics.ListAPIView):
    """
    View for listing all faculty profiles for admin users.
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = Faculty_Profile.objects.all()
    serializer_class = Faculty_ProfileSerializer

    @catch_exception
    def get(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Get list of all faculty profiles.
        
        Returns:
            Response: List of faculty profiles with success message
        """
        faculties = self.get_queryset()
        serialized_faculties = self.get_serializer(faculties, many=True).data
        
        return Message.success('Faculties retrieved successfully', serialized_faculties)


class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting faculty profiles.
    """
    permission_classes = [permissions.IsAdminUser]
    queryset = Faculty_Profile.objects.all()
    serializer_class = Faculty_ProfileSerializer
    lookup_field = 'code'

    @catch_exception
    def get(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Get a specific faculty profile.
        
        Args:
            kwargs: Contains code parameter for lookup
            
        Returns:
            Response: Faculty profile data with success message
        """
        faculty = self.get_object()
        serialized_faculty = self.get_serializer(faculty).data
        
        return Message.success('Faculty retrieved successfully', serialized_faculty)

    @catch_exception
    def patch(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Update a faculty user and profile.
        
        Args:
            request: HTTP request with update data
            kwargs: Contains code parameter for lookup
            
        Returns:
            Response: Success or error message
        """
        # Get and update user data
        code: str = kwargs['code']
        user: User = get_object_or_404(User, code=code)
        serialized_user = UserSerializer(user, data=request.data, partial=True)
        
        if not serialized_user.is_valid():
            return Message.error(serialized_user.errors)

        serialized_user.save()

        # Get and update faculty profile data
        faculty = self.get_object()
        serialized_faculty = self.get_serializer(
            faculty, data=request.data, partial=True)
        
        if not serialized_faculty.is_valid():
            return Message.error(serialized_faculty.errors)

        serialized_faculty.save()
        
        return Message.success('Faculty updated successfully')

    @catch_exception
    def delete(self, request: Any, *args: Any, **kwargs: Any) -> Response:
        """
        Delete a faculty user and profile.
        
        Args:
            kwargs: Contains code parameter for lookup
            
        Returns:
            Response: Success message
        """
        code: str = kwargs['code']
        user: User = get_object_or_404(User, code=code)
        user.delete()  # Cascade delete will remove the profile as well
        
        return Message.success('Faculty deleted successfully')
