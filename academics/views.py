from rest_framework import views, response, permissions
from backend.message import Message
from backend.utils import catch_exception
from .models import Department, Batch, Section, Semester, Semester_Course, Course
from django.shortcuts import get_object_or_404

# Creating new Department api


class AddDepartment(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        Department.objects.get_or_create(
            id=request.data['id'],
            name=request.data['name'],
        )
        return Message.success('Department added successfully')


# Creating new Batch api
class AddBatch(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        department = get_object_or_404(
            Department, id=request.data['department'])

        Batch.objects.get_or_create(
            id=request.data['id'],
            name=request.data['name'],
            department=department,
        )
        return Message.success('Batch added successfully')


# Creating new Section api
class AddSection(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        batch = get_object_or_404(Batch, id=request.data['batch'])

        Section.objects.get_or_create(
            id=request.data['id'],
            name=request.data['name'],
            batch=batch,
        )
        return Message.success('Section added successfully')


# Creating new Semester api
class AddSemester(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        batch = get_object_or_404(Batch, id=request.data['batch'])

        semester = Semester.objects.get_or_create(
            id=request.data['id'],
            name=request.data['name'],
            batch=batch,
        )
        Semester_Course.objects.get_or_create(
            id=request.data['id'],
            semester=semester,
        )
        return Message.success('Semester added successfully')

# Creating new Course to Semester api


class AddCourseToSemester(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        semester_course = get_object_or_404(
            Semester_Course, id=request.data['semester'])
        course = get_object_or_404(Course, id=request.data['course'])

        semester_course.courses.add(course)
        return Message.success('Course added to semester successfully')
