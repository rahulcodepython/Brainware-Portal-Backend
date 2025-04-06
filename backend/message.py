from typing import Dict  # Import for type hinting
from rest_framework import status
from rest_framework.response import Response


class Message:
    # Method to handle unauthorized responses
    def unauthorized(msg: str, data: Dict[str, str] = None) -> Response:
        if data is None:  # Ensure data is not mutable
            data = {}
        response_data = {"error": msg}  # Prepare response data
        response_data.update(data)  # Merge additional data
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

    # Method to handle warning responses
    def warn(msg: str, data: Dict[str, str] = None) -> Response:
        if data is None:
            data = {}
        response_data = {"error": msg}
        response_data.update(data)
        return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)

    # Method to handle error responses
    def error(msg: str, data: Dict[str, str] = None) -> Response:
        if data is None:
            data = {}
        response_data = {"error": msg}
        response_data.update(data)
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    # Method to handle success responses
    def success(msg: str, data: Dict[str, str] = None) -> Response:
        if data is None:
            data = {}
        response_data = {"success": msg}
        response_data.update(data)
        return Response(response_data, status=status.HTTP_200_OK)

    # Method to handle creation success responses
    def create(msg: str, data: Dict[str, str] = None) -> Response:
        if data is None:
            data = {}
        response_data = {"success": msg}
        response_data.update(data)
        return Response(response_data, status=status.HTTP_201_CREATED)
