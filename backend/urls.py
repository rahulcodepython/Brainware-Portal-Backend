from django.contrib import admin
from django.urls import path, include
from django.conf import settings


def url_path(url): return f"{'' if settings.DEBUG else 'api/'}{url}"


urlpatterns = [
    path(url_path('admin/'), admin.site.urls),
    path(url_path('auth/'), include('authentication.urls')),
    path(url_path('academics/'), include('academics.urls')),
    path(url_path('courses/'), include('courses.urls')),
]
