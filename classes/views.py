from rest_framework import views, permissions
from backend.message import Message
from backend.utils import catch_exception
from .serializers import ClassRoutineSerializer, AddLecturePlanSerializer


class AddClassRoutine(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request):
        serialized = ClassRoutineSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success("Class routine added successfully", {"id": serialized.data["id"]})


class AddLecturePlan(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    @catch_exception
    def post(self, request):
        serialized = AddLecturePlanSerializer(data=request.data)

        if not serialized.is_valid():
            return Message.error(serialized.errors)

        serialized.save()
        return Message.success("Lecture plan added successfully")
