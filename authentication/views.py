from rest_framework import views, response, permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from backend.message import Message
from backend.utils import catch_exception
from authentication.models import User, Student_Profile, Faculty_Profile
from academics.models import Section, Semester
from django.shortcuts import get_object_or_404
from academics.models import Department


class Login(views.APIView):
    permission_classes = [permissions.AllowAny]

    @catch_exception
    def post(self, request, *args, **kwargs):
        code = request.data['code']
        password = request.data['password']

        user = authenticate(request, username=code, password=password)

        if user is None:
            return response.Response(Message.unauthorized('Invalid credentials'))

        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        res = response.Response(
            {"refresh": str(refresh), "access": access}, status=status.HTTP_200_OK)
        res.set_cookie('refresh', str(refresh),
                       httponly=True, secure=True, samesite='None')

        return res


class AddStudent(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        section = get_object_or_404(Section, id=request.data['section'])
        semester = get_object_or_404(
            Semester, id=request.data['current_semester'])

        user = User.objects.create_user(
            code=request.data['code'],
            password=request.data['password'],
            is_active=True,
            is_staff=False
        )
        Student_Profile.objects.create(
            user=user,
            name=request.data['name'],
            email=request.data['email'],
            gender=request.data['gender'],
            section=section,
            current_semester=semester,
        )
        return Message.success('Student added successfully')


class AddFaculty(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        department = get_object_or_404(
            Department, id=request.data['department'])

        user = User.objects.create_user(
            code=request.data['code'],
            password=request.data['password'],
            is_active=True,
            is_staff=False
        )
        Faculty_Profile.objects.create(
            user=user,
            name=request.data['name'],
            email=request.data['email'],
            gender=request.data['gender'],
            department=department,
        )
        return Message.success('Faculty added successfully')
