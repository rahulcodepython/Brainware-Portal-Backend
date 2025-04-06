from typing import Callable, Any  # Importing necessary types for type hinting
from .message import Message  # Importing the Message class for error handling


def catch_exception(func: Callable) -> Callable:
    """
    A decorator to catch exceptions in the wrapped function and return an error message.

    Args:
        func (Callable): The function to be wrapped.

    Returns:
        Callable: The wrapped function with exception handling.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function to execute the original function with exception handling.

        Args:
            *args (Any): Positional arguments for the wrapped function.
            **kwargs (Any): Keyword arguments for the wrapped function.

        Returns:
            Any: The result of the wrapped function or an error message in case of an exception.
        """
        try:
            # Attempt to execute the original function
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            # Handle any exception that occurs and log the error
            error_message = f"Error in {func.__name__}: {e}"
            print(error_message)  # Log the error for debugging
            # Return an error message using the Message class
            return Message.error(str(e))

    return wrapper
