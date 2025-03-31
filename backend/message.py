from rest_framework import status
from rest_framework.response import Response


class Message:
    def unauthorized(msg: str, data: dict = {}) -> Response:
        return Response({"error": msg} | data, status=status.HTTP_401_UNAUTHORIZED)

    def warn(msg: str, data: dict = {}) -> Response:
        return Response({"error": msg} | data, status=status.HTTP_406_NOT_ACCEPTABLE)

    def error(msg: str, data: dict = {}) -> Response:
        return Response({"error": msg} | data, status=status.HTTP_400_BAD_REQUEST)

    def success(msg: str, data: dict = {}) -> Response:
        return Response({"success": msg} | data, status=status.HTTP_200_OK)

    def create(msg: str, data: dict = {}) -> Response:
        return Response({"success": msg} | data, status=status.HTTP_201_CREATED)
