from rest_framework import views, status, response, permissions
from academics.models import Department, Batch, Section, Semester
from courses.models import Course, Module, Lecture


class Index(views.APIView):
    """
    Index view for the API.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return response.Response({"message": "Welcome to the API!"}, status=status.HTTP_200_OK)
