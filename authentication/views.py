from rest_framework import views, permissions  # Import necessary modules
from rest_framework_simplejwt.tokens import RefreshToken  # For JWT token generation
from django.contrib.auth import authenticate  # For user authentication
from backend.message import Message  # Custom message utility
from backend.utils import catch_exception  # Custom exception handler
from .serializers import (  # Import serializers
    LoginSerializer,
    UserSerializer,
    Student_ProfileSerializer,
    Faculty_ProfileSerializer,
)
from .models import Student_Profile, Faculty_Profile, User  # Import models
# For fetching objects or returning 404
from django.shortcuts import get_object_or_404


class Login(views.APIView):
    # Allow any user to access
    permission_classes: list = [permissions.AllowAny]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized: LoginSerializer = LoginSerializer(
            data=request.data)  # Serialize input data

        if not serialized.is_valid():  # Check if data is valid
            return Message.error(serialized.errors)

        username: str = serialized.data["code"]
        password: str = serialized.data["password"]
        user: User | None = authenticate(
            username=username, password=password)  # Authenticate user

        if user is None:  # If authentication fails
            return Message.error('Invalid credentials.')

        refresh: RefreshToken = RefreshToken.for_user(
            user)  # Generate refresh token
        access: str = str(refresh.access_token)  # Generate access token

        return Message.success('Login successful', {"refresh": str(refresh), "access": access})


class AddStudent(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized_user: UserSerializer = UserSerializer(
            data=request.data)  # Serialize user data

        if not serialized_user.is_valid():  # Validate user data
            return Message.error(serialized_user.errors)

        user: User = serialized_user.save()  # Save user instance

        serialized_student: Student_ProfileSerializer = Student_ProfileSerializer(
            data=request.data)  # Serialize student data

        if not serialized_student.is_valid():  # Validate student data
            return Message.error(serialized_student.errors)

        # Save student profile linked to user
        serialized_student.save(user=user)

        return Message.success('Student added successfully')


class StudentList(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, *args, **kwargs):
        students: list = Student_Profile.objects.all()  # Fetch all student profiles
        serialized_students: list = Student_ProfileSerializer(
            students, many=True).data  # Serialize student profiles
        return Message.success('Students retrieved successfully', serialized_students)


class StudentDetail(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, code: str, *args, **kwargs):
        student: Student_Profile = get_object_or_404(
            Student_Profile, code=code)  # Fetch student by code
        serialized_student: dict = Student_ProfileSerializer(
            student).data  # Serialize student data
        return Message.success('Student retrieved successfully', serialized_student)

    @catch_exception
    def patch(self, request, code: str, *args, **kwargs):
        user: User = get_object_or_404(User, code=code)  # Fetch user by code
        serialized_user: UserSerializer = UserSerializer(
            user, data=request.data, partial=True)  # Serialize user data

        if not serialized_user.is_valid():  # Validate user data
            return Message.error(serialized_user.errors)

        serialized_user.save()  # Save updated user data

        student: Student_Profile = get_object_or_404(
            Student_Profile, code=code)  # Fetch student profile
        serialized_student: Student_ProfileSerializer = Student_ProfileSerializer(
            student, data=request.data, partial=True)  # Serialize student data

        if not serialized_student.is_valid():  # Validate student data
            return Message.error(serialized_student.errors)

        serialized_student.save()  # Save updated student profile

        return Message.success('Student updated successfully')

    @catch_exception
    def delete(self, request, code: str, *args, **kwargs):
        user: User = get_object_or_404(User, code=code)  # Fetch user by code
        user.delete()  # Delete user
        return Message.success('Student deleted successfully')


class AddFaculty(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized_user: UserSerializer = UserSerializer(
            data=request.data)  # Serialize user data

        if not serialized_user.is_valid():  # Validate user data
            return Message.error(serialized_user.errors)

        user: User = serialized_user.save()  # Save user instance

        serialized_faculty: Faculty_ProfileSerializer = Faculty_ProfileSerializer(
            data=request.data)  # Serialize faculty data

        if not serialized_faculty.is_valid():  # Validate faculty data
            return Message.error(serialized_faculty.errors)

        # Save faculty profile linked to user
        serialized_faculty.save(user=user)

        return Message.success('Faculty added successfully')


class FacultyList(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, *args, **kwargs):
        faculties: list = Faculty_Profile.objects.all()  # Fetch all faculty profiles
        serialized_faculties: list = Faculty_ProfileSerializer(
            faculties, many=True).data  # Serialize faculty profiles
        return Message.success('Faculties retrieved successfully', serialized_faculties)


class FacultyDetail(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, code: str, *args, **kwargs):
        faculty: Faculty_Profile = get_object_or_404(
            Faculty_Profile, code=code)  # Fetch faculty by code
        serialized_faculty: dict = Faculty_ProfileSerializer(
            faculty).data  # Serialize faculty data
        return Message.success('Faculty retrieved successfully', serialized_faculty)

    @catch_exception
    def patch(self, request, code: str, *args, **kwargs):
        user: User = get_object_or_404(User, code=code)  # Fetch user by code
        serialized_user: UserSerializer = UserSerializer(
            user, data=request.data, partial=True)  # Serialize user data

        if not serialized_user.is_valid():  # Validate user data
            return Message.error(serialized_user.errors)

        serialized_user.save()  # Save updated user data

        faculty: Faculty_Profile = get_object_or_404(
            Faculty_Profile, code=code)  # Fetch faculty profile
        serialized_faculty: Faculty_ProfileSerializer = Faculty_ProfileSerializer(
            faculty, data=request.data, partial=True)  # Serialize faculty data

        if not serialized_faculty.is_valid():  # Validate faculty data
            return Message.error(serialized_faculty.errors)

        serialized_faculty.save()  # Save updated faculty profile

        return Message.success('Faculty updated successfully')

    @catch_exception
    def delete(self, request, code: str, *args, **kwargs):
        user: User = get_object_or_404(User, code=code)  # Fetch user by code
        user.delete()  # Delete user
        return Message.success('Faculty deleted successfully')
