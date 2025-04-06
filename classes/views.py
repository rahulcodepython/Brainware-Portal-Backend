from rest_framework.views import APIView  # Import only what is needed
from rest_framework.permissions import IsAdminUser, IsAuthenticated
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


class AddClassRoutine(APIView):
    permission_classes = [IsAdminUser]  # Restrict access to admin users

    @catch_exception
    def post(self, request) -> Message:
        # Serialize the incoming request data
        serialized = ClassRoutineSerializer(data=request.data)

        # Check if the serialized data is valid
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the serialized data to the database
        serialized.save()
        return Message.success(
            "Class routine added successfully",
            {"id": serialized.data["id"]}
        )


class ClassRoutines(APIView):
    permission_classes = [IsAdminUser]

    @catch_exception
    def get(self, request, section: int) -> Message:
        # Fetch the section object or return a 404 error
        section_obj = get_object_or_404(Section, id=section)

        # Filter class routines based on section and semester
        class_routines_queryset = Class_Routine.objects.filter(
            section=section_obj,
            semester=section_obj.batch.current_semester
        )

        # Serialize the filtered class routines
        serialized = ClassRoutineSerializer(class_routines_queryset, many=True)

        return Message.success(
            "Class routines fetched successfully",
            serialized.data
        )


class ClassRoutine(APIView):
    permission_classes = [IsAdminUser]

    @catch_exception
    def get(self, request, id: int) -> Message:
        # Fetch the class routine object or return a 404 error
        class_routine = get_object_or_404(Class_Routine, id=id)

        # Serialize the class routine
        serialized = ClassRoutineSerializer(class_routine)

        return Message.success(
            "Class routine fetched successfully",
            serialized.data
        )

    @catch_exception
    def patch(self, request, id: int) -> Message:
        # Fetch the class routine object or return a 404 error
        class_routine = get_object_or_404(Class_Routine, id=id)

        # Serialize the incoming data for partial update
        serialized = ClassRoutineSerializer(
            class_routine,
            data=request.data,
            partial=True
        )

        # Check if the serialized data is valid
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the updated data to the database
        serialized.save()
        return Message.success(
            "Class routine updated successfully",
            serialized.data
        )

    @catch_exception
    def delete(self, request, id: int) -> Message:
        # Fetch the class routine object or return a 404 error
        class_routine = get_object_or_404(Class_Routine, id=id)

        # Delete the class routine
        class_routine.delete()

        return Message.success("Class routine deleted successfully")


class AddLecturePlan(APIView):
    permission_classes = [IsAdminUser]

    @catch_exception
    def post(self, request) -> Message:
        # Serialize the incoming request data
        serialized = AddLecturePlanSerializer(data=request.data)

        # Check if the serialized data is valid
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the serialized data to the database
        serialized.save()
        return Message.success("Lecture plan added successfully")


class LecturePlans(APIView):
    permission_classes = [IsAdminUser]

    @catch_exception
    def get(self, request, section: int, course: int) -> Message:
        # Fetch the section object or return a 404 error
        section_obj = get_object_or_404(Section, id=section)

        # Filter lecture plans based on section, course, and semester
        lecture_plans_queryset = LecturePlan.objects.filter(
            section=section_obj,
            cours=course,
            semester=section_obj.batch.current_semester
        )

        # Serialize the filtered lecture plans
        serialized = AddLecturePlanSerializer(
            lecture_plans_queryset, many=True)

        return Message.success(
            "Lecture plans fetched successfully",
            serialized.data
        )


class LecturePlan(APIView):
    permission_classes = [IsAdminUser]

    @catch_exception
    def get(self, request, id: int) -> Message:
        # Fetch the lecture plan object or return a 404 error
        lecture_plan = get_object_or_404(LecturePlan, id=id)

        # Serialize the lecture plan
        serialized = AddLecturePlanSerializer(lecture_plan)

        return Message.success(
            "Lecture plan fetched successfully",
            serialized.data
        )

    @catch_exception
    def patch(self, request, id: int) -> Message:
        # Fetch the lecture plan object or return a 404 error
        lecture_plan = get_object_or_404(LecturePlan, id=id)

        # Serialize the incoming data for partial update
        serialized = AddLecturePlanSerializer(
            LecturePlan,
            data=request.data,
            partial=True
        )

        # Check if the serialized data is valid
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the updated data to the database
        serialized.save()
        return Message.success(
            "Lecture plan updated successfully",
            serialized.data
        )

    @catch_exception
    def delete(self, request, id: int) -> Message:
        # Fetch the lecture plan object or return a 404 error
        lecture_plan = get_object_or_404(LecturePlan, id=id)

        # Delete the lecture plan
        lecture_plan.delete()

        return Message.success("Lecture plan deleted successfully")


class RegisterAttendance(APIView):
    permission_classes = [IsAuthenticated]  # Allow only authenticated users

    @catch_exception
    def post(self, request) -> Message:
        # Serialize the incoming request data
        serialized = AttendanceSerializer(data=request.data)

        # Check if the serialized data is valid
        if not serialized.is_valid():
            return Message.error(serialized.errors)

        # Save the serialized data to the database
        serialized.save()
        return Message.success("Attendance registered successfully.")
