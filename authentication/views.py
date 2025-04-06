from rest_framework import views, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from backend.message import Message
from backend.utils import catch_exception
from .serializers import (
    LoginSerializer,
    UserSerializer,
    Student_ProfileSerializer,
    Faculty_ProfileSerializer,
)
from .models import Student_Profile, Faculty_Profile, User
from django.shortcuts import get_object_or_404


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


class StudentList(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, *args, **kwargs):
        students = Student_ProfileSerializer(
            Student_Profile.objects.all(), many=True).data
        return Message.success('Students retrieved successfully', students)


class StudentDetail(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, code, *args, **kwargs):
        student = get_object_or_404(Student_Profile, code=code)
        serialized = Student_ProfileSerializer(student).data
        return Message.success('Student retrieved successfully', serialized)

    @catch_exception
    def patch(self, request, code, *args, **kwargs):
        user = get_object_or_404(User, code=code)
        serialized = UserSerializer(
            user, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        student = get_object_or_404(Student_Profile, code=code)
        serialized = Student_ProfileSerializer(
            student, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success('Student updated successfully')

    @catch_exception
    def delete(self, request, code, *args, **kwargs):
        user = get_object_or_404(User, code=code)
        user.delete()
        return Message.success('Student deleted successfully')


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


class FacultyList(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, *args, **kwargs):
        faculties = Faculty_ProfileSerializer(
            Faculty_Profile.objects.all(), many=True).data
        return Message.success('Faculties retrieved successfully', faculties)


class FacultyDetail(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, code, *args, **kwargs):
        faculty = get_object_or_404(Faculty_Profile, code=code)
        serialized = Faculty_ProfileSerializer(faculty).data
        return Message.success('Faculty retrieved successfully', serialized)

    @catch_exception
    def patch(self, request, code, *args, **kwargs):
        user = get_object_or_404(User, code=code)
        serialized = UserSerializer(
            user, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        faculty = get_object_or_404(Faculty_Profile, code=code)
        serialized = Faculty_ProfileSerializer(
            faculty, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()

        return Message.success('Faculty updated successfully')

    @catch_exception
    def delete(self, request, code, *args, **kwargs):
        user = get_object_or_404(User, code=code)
        user.delete()
        return Message.success('Faculty deleted successfully')
