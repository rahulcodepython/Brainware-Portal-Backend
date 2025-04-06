from rest_framework import generics, permissions
from rest_framework.response import Response
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


class Login(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = self.get_serializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        username = serialized.data["code"]
        password = serialized.data["password"]
        user = authenticate(username=username, password=password)

        if user is None:
            return Message.error('Invalid credentials.')

        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        return Message.success('Login successful', {"refresh": str(refresh), "access": access})


class AddStudent(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized_user = self.get_serializer(data=request.data)

        if not serialized_user.is_valid():
            return Message.error(serialized_user.errors)

        user = serialized_user.save()

        serialized_student = Student_ProfileSerializer(data=request.data)

        if not serialized_student.is_valid():
            return Message.error(serialized_student.errors)

        serialized_student.save(user=user)

        return Message.success('Student added successfully')


class StudentList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Student_Profile.objects.all()
    serializer_class = Student_ProfileSerializer

    @catch_exception
    def get(self, request, *args, **kwargs):
        students = self.get_queryset()
        serialized_students = self.get_serializer(students, many=True).data
        return Message.success('Students retrieved successfully', serialized_students)


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Student_Profile.objects.all()
    serializer_class = Student_ProfileSerializer
    lookup_field = 'code'

    @catch_exception
    def get(self, request, *args, **kwargs):
        student = self.get_object()
        serialized_student = self.get_serializer(student).data
        return Message.success('Student retrieved successfully', serialized_student)

    @catch_exception
    def patch(self, request, *args, **kwargs):
        user = get_object_or_404(User, code=kwargs['code'])
        serialized_user = UserSerializer(user, data=request.data, partial=True)

        if not serialized_user.is_valid():
            return Message.error(serialized_user.errors)

        serialized_user.save()

        student = self.get_object()
        serialized_student = self.get_serializer(
            student, data=request.data, partial=True)

        if not serialized_student.is_valid():
            return Message.error(serialized_student.errors)

        serialized_student.save()

        return Message.success('Student updated successfully')

    @catch_exception
    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, code=kwargs['code'])
        user.delete()
        return Message.success('Student deleted successfully')


class AddFaculty(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized_user = self.get_serializer(data=request.data)

        if not serialized_user.is_valid():
            return Message.error(serialized_user.errors)

        user = serialized_user.save()

        serialized_faculty = Faculty_ProfileSerializer(data=request.data)

        if not serialized_faculty.is_valid():
            return Message.error(serialized_faculty.errors)

        serialized_faculty.save(user=user)

        return Message.success('Faculty added successfully')


class FacultyList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Faculty_Profile.objects.all()
    serializer_class = Faculty_ProfileSerializer

    @catch_exception
    def get(self, request, *args, **kwargs):
        faculties = self.get_queryset()
        serialized_faculties = self.get_serializer(faculties, many=True).data
        return Message.success('Faculties retrieved successfully', serialized_faculties)


class FacultyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Faculty_Profile.objects.all()
    serializer_class = Faculty_ProfileSerializer
    lookup_field = 'code'

    @catch_exception
    def get(self, request, *args, **kwargs):
        faculty = self.get_object()
        serialized_faculty = self.get_serializer(faculty).data
        return Message.success('Faculty retrieved successfully', serialized_faculty)

    @catch_exception
    def patch(self, request, *args, **kwargs):
        user = get_object_or_404(User, code=kwargs['code'])
        serialized_user = UserSerializer(user, data=request.data, partial=True)

        if not serialized_user.is_valid():
            return Message.error(serialized_user.errors)

        serialized_user.save()

        faculty = self.get_object()
        serialized_faculty = self.get_serializer(
            faculty, data=request.data, partial=True)

        if not serialized_faculty.is_valid():
            return Message.error(serialized_faculty.errors)

        serialized_faculty.save()

        return Message.success('Faculty updated successfully')

    @catch_exception
    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, code=kwargs['code'])
        user.delete()
        return Message.success('Faculty deleted successfully')
