from django.contrib import admin  # Import admin module for admin site
from django.urls import path, include  # Import path and include for URL routing
from django.conf import settings  # Import settings to access DEBUG flag
from typing import List, Callable  # Import type hints
from .views import Index  # Import Index view for the root URLs


def url_path(url: str) -> str:
    """
    Generate URL path prefix based on DEVELOPMENT mode.

    Args:
        url: The URL suffix to append to the prefix

    Returns:
        Full URL path with appropriate prefix based on DEVELOPMENT mode
    """
    # Check if DEVELOPMENT setting exists before using it
    development_enabled: bool = getattr(settings, 'DEVELOPMENT', False)
    # Return URL with prefix only in production
    prefix: str = '' if development_enabled else 'api/'
    return f"{prefix}{url}"


# Define URL pattern components for better readability
admin_path: str = url_path('admin/')  # Admin URL path
# root_path: str = url_path('')  # Root URL path
auth_path: str = url_path('auth/')  # Authentication URL path
academics_path: str = url_path('academics/')  # Academics URL path
courses_path: str = url_path('courses/')  # Courses URL path
classes_path: str = url_path('classes/')  # Classes URL path

# Define URL patterns
urlpatterns: List[Callable] = [
    path(admin_path, admin.site.urls),  # Admin site URL
    # path(root_path, Index.as_view(), name='index'),  # Root URL for Index view
    path("", include("frontend.urls")),  # Include frontend URLs
    path(auth_path, include('authentication.urls')),  # Authentication app URLs
    path(academics_path, include('academics.urls')),  # Academics app URLs
    path(courses_path, include('courses.urls')),  # Courses app URLs
    path(classes_path, include('classes.urls')),  # Classes app URLs
]
