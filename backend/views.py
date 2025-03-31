from rest_framework import views, status, response


class Index(views.APIView):
    """
    Index view for the API.
    """

    def get(self, request, *args, **kwargs):
        return response.Response({"message": "Welcome to the API!"}, status=status.HTTP_200_OK)
