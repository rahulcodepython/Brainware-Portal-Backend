from rest_framework.generics import GenericAPIView  # Use GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK
from django.conf import settings


# Define the Index view for the API


class Index(GenericAPIView):
    """
    Index view for the API.
    """

    # Allow access to any user (no authentication required)
    permission_classes: list = [AllowAny]

    def get(self, request, *args, **kwargs) -> Response:
        """
        Handle GET requests to return a welcome message.
        """
        # Define the response message
        message: dict = {"message": "Welcome to the API!",
                         "env": settings.ENVIRONMENT}

        # Return the response with a 200 OK status
        return Response(data=message, status=HTTP_200_OK)
