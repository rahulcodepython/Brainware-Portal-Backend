from rest_framework import views, response, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from backend.message import Message
from backend.utils import catch_exception
from authentication.models import User, Student_Profile, Faculty_Profile
from academics.models import Section, Semester
from django.shortcuts import get_object_or_404
from academics.models import Department
from .serializers import (
    LoginSerializer,
    UserSerializer,
    Student_ProfileSerializer,
    Faculty_ProfileSerializer,
)


class Login(views.APIView):
    permission_classes = [permissions.AllowAny]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = LoginSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        user = authenticate(
            username=serialized.data["code"], password=serialized.data["password"])

        if user is None:
            return Message.error('Invalid credentials.')

        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        return Message.success('Login successful', {"refresh": str(refresh), "access": access})


class AddStudent(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = UserSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        user = serialized.save()

        student_serialized = Student_ProfileSerializer(data=request.data)

        if not student_serialized.is_valid():
            return Message.error(student_serialized.errors)

        student_serialized.save(user=user)

        return Message.success('Student added successfully')


class AddFaculty(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = UserSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        user = serialized.save()

        faculty_serialized = Faculty_ProfileSerializer(data=request.data)

        if not faculty_serialized.is_valid():
            return Message.error(faculty_serialized.errors)

        faculty_serialized.save(user=user)

        return Message.success('Faculty added successfully')
