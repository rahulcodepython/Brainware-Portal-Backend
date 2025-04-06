from django.contrib import admin  # Import admin module for admin site
from django.urls import path, include  # Import path and include for URL routing
from django.conf import settings  # Import settings to access DEBUG flag
from .views import Index  # Import Index view for the root URL

# Function to generate URL paths based on DEBUG mode


def url_path(url: str) -> str:
    """Generate URL path prefix based on DEBUG mode."""
    return f"{'' if settings.DEBUG else 'api/'}{url}"


# Define URL patterns
urlpatterns: list = [
    path(url_path('admin/'), admin.site.urls),  # Admin site URL
    # Root URL for Index view
    path(url_path(''), Index.as_view(), name='index'),
    # Authentication app URLs
    path(url_path('auth/'), include('authentication.urls')),
    path(url_path('academics/'), include('academics.urls')),  # Academics app URLs
    path(url_path('courses/'), include('courses.urls')),  # Courses app URLs
    path(url_path('classes/'), include('classes.urls')),  # Classes app URLs
]

# Ensure runtime error handling for missing settings
if not hasattr(settings, 'DEBUG'):
    raise RuntimeError(
        "The 'DEBUG' setting is not defined in the Django settings.")
