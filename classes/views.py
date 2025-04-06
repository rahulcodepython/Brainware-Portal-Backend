from rest_framework import views, permissions
from backend.message import Message
from backend.utils import catch_exception
from .serializers import (
    ClassRoutineSerializer,
    AddLecturePlanSerializer,
    AttendanceSerializer
)
from .models import Class_Routine, Lecture_Plan
from django.shortcuts import get_object_or_404
from academics.models import Section


class AddClassRoutine(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request):
        serialized = ClassRoutineSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success("Class routine added successfully", {"id": serialized.data["id"]})


class ClassRoutines(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, section):
        section = get_object_or_404(Section, id=section)
        class_routines = ClassRoutineSerializer(
            Class_Routine.objects.filter(section=section, semester=section.batch.current_semester), many=True)

        return Message.success("Class routines fetched successfully", class_routines.data)


class ClassRoutine(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, id):
        class_routine = get_object_or_404(Class_Routine, id=id)
        serialized = ClassRoutineSerializer(class_routine)

        return Message.success("Class routine fetched successfully", serialized.data)

    @catch_exception
    def patch(self, request, id):
        class_routine = get_object_or_404(Class_Routine, id=id)
        serialized = ClassRoutineSerializer(
            class_routine, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success("Class routine updated successfully", serialized.data)

    @catch_exception
    def delete(self, request, id):
        class_routine = get_object_or_404(Class_Routine, id=id)
        class_routine.delete()

        return Message.success("Class routine deleted successfully")


class AddLecturePlan(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request):
        serialized = AddLecturePlanSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success("Lecture plan added successfully")


class LecturePlans(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, section, course):
        section = get_object_or_404(Section, id=section)
        lecture_plans = AddLecturePlanSerializer(
            Lecture_Plan.objects.filter(section=section, cours=course, semester=section.batch.current_semester), many=True)

        return Message.success("Lecture plans fetched successfully", lecture_plans.data)


class LecturePlan(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def get(self, request, id):
        lecture_plan = get_object_or_404(Lecture_Plan, id=id)
        serialized = AddLecturePlanSerializer(lecture_plan)

        return Message.success("Lecture plan fetched successfully", serialized.data)

    @catch_exception
    def patch(self, request, id):
        lecture_plan = get_object_or_404(Lecture_Plan, id=id)
        serialized = AddLecturePlanSerializer(
            lecture_plan, data=request.data, partial=True)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success("Lecture plan updated successfully", serialized.data)

    @catch_exception
    def delete(self, request, id):
        lecture_plan = get_object_or_404(Lecture_Plan, id=id)
        lecture_plan.delete()

        return Message.success("Lecture plan deleted successfully")


class RegisterAttendance(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    @catch_exception
    def post(self, request, *args, **kwargs):
        serialized = AttendanceSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success("Attendance registered successfully.")
