# Importing necessary modules from DRF
from rest_framework import views, permissions
from backend.message import Message  # Custom message handling
from backend.utils import catch_exception  # Custom exception handling decorator
# Helper for fetching objects or returning 404
from django.shortcuts import get_object_or_404
from .models import Course, Module, Lecture  # Importing models
# Importing serializers
from .serializers import CourseSerializer, ModuleSerializer, LectureSerializer


# API View for creating a course
class CreateCourse(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        # Serialize incoming data
        serialized: CourseSerializer = CourseSerializer(data=request.data)

        # Validate serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the course if valid
        serialized.save()

        return Message.success("Course created successfully.")


# API View for listing all courses
class CourseList(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, *args, **kwargs):
        # Fetch all courses
        courses: list = Course.objects.all()

        # Serialize the list of courses
        serialized: CourseSerializer = CourseSerializer(courses, many=True)

        return Message.success(serialized.data)


# API View for retrieving, updating, or deleting a specific course
class CourseDetail(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, id: int, *args, **kwargs):
        # Fetch the course by ID or return 404
        course: Course = get_object_or_404(Course, id=id)

        # Serialize the course
        serialized: CourseSerializer = CourseSerializer(course)

        return Message.success(serialized.data)

    @catch_exception
    def patch(self, request, id: int, *args, **kwargs):
        # Fetch the course by ID or return 404
        course: Course = get_object_or_404(Course, id=id)

        # Serialize the course with partial update
        serialized: CourseSerializer = CourseSerializer(
            course, data=request.data, partial=True)

        # Validate serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the updated course
        serialized.save()

        return Message.success("Course updated successfully.")

    @catch_exception
    def delete(self, request, id: int, *args, **kwargs):
        # Fetch the course by ID or return 404
        course: Course = get_object_or_404(Course, id=id)

        # Delete the course
        course.delete()

        return Message.success("Course deleted successfully.")


# API View for creating a module
class CreateModule(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        # Serialize incoming data
        serialized: ModuleSerializer = ModuleSerializer(data=request.data)

        # Validate serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the module if valid
        serialized.save()

        return Message.success("Module created successfully.")


# API View for listing all modules
class ModuleList(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, *args, **kwargs):
        # Fetch all modules
        modules: list = Module.objects.all()

        # Serialize the list of modules
        serialized: ModuleSerializer = ModuleSerializer(modules, many=True)

        return Message.success(serialized.data)


# API View for retrieving, updating, or deleting a specific module
class ModuleDetail(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, id: int, *args, **kwargs):
        # Fetch the module by ID or return 404
        module: Module = get_object_or_404(Module, id=id)

        # Serialize the module
        serialized: ModuleSerializer = ModuleSerializer(module)

        return Message.success(serialized.data)

    @catch_exception
    def patch(self, request, id: int, *args, **kwargs):
        # Fetch the module by ID or return 404
        module: Module = get_object_or_404(Module, id=id)

        # Serialize the module with partial update
        serialized: ModuleSerializer = ModuleSerializer(
            module, data=request.data, partial=True)

        # Validate serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the updated module
        serialized.save()

        return Message.success("Module updated successfully.")

    @catch_exception
    def delete(self, request, id: int, *args, **kwargs):
        # Fetch the module by ID or return 404
        module: Module = get_object_or_404(Module, id=id)

        # Delete the module
        module.delete()

        return Message.success("Module deleted successfully.")


# API View for creating a lecture
class CreateLecture(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request, *args, **kwargs):
        # Serialize incoming data
        serialized: LectureSerializer = LectureSerializer(data=request.data)

        # Validate serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the lecture if valid
        serialized.save()

        return Message.success("Lecture created successfully.")


# API View for listing all lectures
class LectureList(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, *args, **kwargs):
        # Fetch all lectures
        lectures: list = Lecture.objects.all()

        # Serialize the list of lectures
        serialized: LectureSerializer = LectureSerializer(lectures, many=True)

        return Message.success(serialized.data)


# API View for retrieving, updating, or deleting a specific lecture
class LectureDetail(views.APIView):
    # Restrict access to admin users
    permission_classes: list = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, id: int, *args, **kwargs):
        # Fetch the lecture by ID or return 404
        lecture: Lecture = get_object_or_404(Lecture, id=id)

        # Serialize the lecture
        serialized: LectureSerializer = LectureSerializer(lecture)

        return Message.success(serialized.data)

    @catch_exception
    def patch(self, request, id: int, *args, **kwargs):
        # Fetch the lecture by ID or return 404
        lecture: Lecture = get_object_or_404(Lecture, id=id)

        # Serialize the lecture with partial update
        serialized: LectureSerializer = LectureSerializer(
            lecture, data=request.data, partial=True)

        # Validate serialized data
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the updated lecture
        serialized.save()

        return Message.success("Lecture updated successfully.")

    @catch_exception
    def delete(self, request, id: int, *args, **kwargs):
        # Fetch the lecture by ID or return 404
        lecture: Lecture = get_object_or_404(Lecture, id=id)

        # Delete the lecture
        lecture.delete()

        return Message.success("Lecture deleted successfully.")
