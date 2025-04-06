from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView
)
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


class AddClassRoutine(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ClassRoutineSerializer

    @catch_exception
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Message.error(serializer.errors)
        serializer.save()
        return Message.success(
            "Class routine added successfully",
            {"id": serializer.data["id"]}
        )


class ClassRoutines(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ClassRoutineSerializer

    @catch_exception
    def list(self, request, *args, **kwargs):
        section_id = kwargs.get('section')
        section_obj = get_object_or_404(Section, id=section_id)
        queryset = Class_Routine.objects.filter(
            section=section_obj,
            semester=section_obj.batch.current_semester
        )
        serializer = self.get_serializer(queryset, many=True)
        return Message.success(
            "Class routines fetched successfully",
            serializer.data
        )


class ClassRoutine(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ClassRoutineSerializer
    queryset = Class_Routine.objects.all()

    @catch_exception
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Message.success(
            "Class routine fetched successfully",
            serializer.data
        )

    @catch_exception
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Message.error(serializer.errors)
        serializer.save()
        return Message.success(
            "Class routine updated successfully",
            serializer.data
        )

    @catch_exception
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Message.success("Class routine deleted successfully")


class AddLecturePlan(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AddLecturePlanSerializer

    @catch_exception
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Message.error(serializer.errors)
        serializer.save()
        return Message.success("Lecture plan added successfully")


class LecturePlans(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AddLecturePlanSerializer

    @catch_exception
    def list(self, request, *args, **kwargs):
        section_id = kwargs.get('section')
        course_id = kwargs.get('course')
        section_obj = get_object_or_404(Section, id=section_id)
        queryset = LecturePlan.objects.filter(
            section=section_obj,
            cours=course_id,
            semester=section_obj.batch.current_semester
        )
        serializer = self.get_serializer(queryset, many=True)
        return Message.success(
            "Lecture plans fetched successfully",
            serializer.data
        )


class LecturePlan(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = AddLecturePlanSerializer
    queryset = LecturePlan.objects.all()

    @catch_exception
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Message.success(
            "Lecture plan fetched successfully",
            serializer.data
        )

    @catch_exception
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        if not serializer.is_valid():
            return Message.error(serializer.errors)
        serializer.save()
        return Message.success(
            "Lecture plan updated successfully",
            serializer.data
        )

    @catch_exception
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Message.success("Lecture plan deleted successfully")


class RegisterAttendance(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AttendanceSerializer

    @catch_exception
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Message.error(serializer.errors)
        serializer.save()
        return Message.success("Attendance registered successfully.")
