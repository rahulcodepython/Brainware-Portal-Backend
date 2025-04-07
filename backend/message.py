from typing import Dict, Optional, Any  # Import for type hinting
from rest_framework import status
from rest_framework.response import Response


class Message:
    """
    Utility class for standardized API responses with different status codes.
    Contains static methods to generate consistent response objects.
    """

    @staticmethod
    def unauthorized(msg: str, data: Optional[Dict[str, Any]] = None) -> Response:
        """
        Creates a response with 401 Unauthorized status code.

        Args:
            msg (str): Error message to include in response
            data (Optional[Dict[str, Any]]): Additional data to include in response

        Returns:
            Response: DRF Response object with error message and 401 status
        """
        # Initialize empty dict if none provided
        data_dict: Dict[str, Any] = {} if data is None else data
        # Create the base response dictionary with error message
        response_data: Dict[str, Any] = {"error": msg}
        # Add any additional data to the response
        response_data.update(data_dict)
        # Return formatted response with appropriate status code
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def warn(msg: str, data: Optional[Dict[str, Any]] = None) -> Response:
        """
        Creates a response with 406 Not Acceptable status code.

        Args:
            msg (str): Warning message to include in response
            data (Optional[Dict[str, Any]]): Additional data to include in response

        Returns:
            Response: DRF Response object with error message and 406 status
        """
        data_dict: Dict[str, Any] = {} if data is None else data
        response_data: Dict[str, Any] = {"error": msg}
        response_data.update(data_dict)
        return Response(response_data, status=status.HTTP_406_NOT_ACCEPTABLE)

    @staticmethod
    def error(msg: str, data: Optional[Dict[str, Any]] = None) -> Response:
        """
        Creates a response with 400 Bad Request status code.

        Args:
            msg (str): Error message to include in response
            data (Optional[Dict[str, Any]]): Additional data to include in response

        Returns:
            Response: DRF Response object with error message and 400 status
        """
        data_dict: Dict[str, Any] = {} if data is None else data
        response_data: Dict[str, Any] = {"error": msg}
        response_data.update(data_dict)
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def success(msg: str, data: Optional[Dict[str, Any]] = None) -> Response:
        """
        Creates a response with 200 OK status code.

        Args:
            msg (str): Success message to include in response
            data (Optional[Dict[str, Any]]): Additional data to include in response

        Returns:
            Response: DRF Response object with success message and 200 status
        """
        data_dict: Dict[str, Any] = {} if data is None else data
        response_data: Dict[str, Any] = {"success": msg}
        response_data.update(data_dict)
        return Response(response_data, status=status.HTTP_200_OK)

    @staticmethod
    def create(msg: str, data: Optional[Dict[str, Any]] = None) -> Response:
        """
        Creates a response with 201 Created status code.

        Args:
            msg (str): Success message to include in response
            data (Optional[Dict[str, Any]]): Additional data to include in response

        Returns:
            Response: DRF Response object with success message and 201 status
        """
        data_dict: Dict[str, Any] = {} if data is None else data
        response_data: Dict[str, Any] = {"success": msg}
        response_data.update(data_dict)
        return Response(response_data, status=status.HTTP_201_CREATED)
