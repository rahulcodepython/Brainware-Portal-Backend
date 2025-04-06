from rest_framework.views import APIView  # Import only what's needed
from rest_framework.response import Response  # Import Response directly
# Import specific permission class
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK  # Import specific status code

# Define the Index view for the API


class Index(APIView):
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
        message: dict = {"message": "Welcome to the API!"}

        # Return the response with a 200 OK status
        return Response(data=message, status=HTTP_200_OK)
