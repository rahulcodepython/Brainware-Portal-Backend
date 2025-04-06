from django.urls import path  # Importing path for URL routing
from . import views  # Importing views to connect URLs to view classes

# Define URL patterns for the authentication app
urlpatterns: list[path] = [
    # Login URL
    path(
        'login/',  # URL endpoint for login
        views.Login.as_view(),  # View class handling login
        name='login'  # Name for reverse URL resolution
    ),

    # Add student URL
    path(
        'add-student/',  # URL endpoint for adding a student
        views.AddStudent.as_view(),  # View class handling student addition
        name='add_student'  # Name for reverse URL resolution
    ),

    # List students URL
    path(
        'students/',  # URL endpoint for listing students
        views.StudentList.as_view(),  # View class handling student listing
        name='student_list'  # Name for reverse URL resolution
    ),

    # Student detail URL
    path(
        'student/<str:code>/',  # URL endpoint for student details with a dynamic string parameter
        views.StudentDetail.as_view(),  # View class handling student details
        name='student_detail'  # Name for reverse URL resolution
    ),

    # Add faculty URL
    path(
        'add-faculty/',  # URL endpoint for adding a faculty
        views.AddFaculty.as_view(),  # View class handling faculty addition
        name='add_faculty'  # Name for reverse URL resolution
    ),

    # List faculties URL
    path(
        'facultys/',  # URL endpoint for listing faculties
        views.FacultyList.as_view(),  # View class handling faculty listing
        name='faculty_list'  # Name for reverse URL resolution
    ),

    # Faculty detail URL
    path(
        'faculty/<str:code>/',  # URL endpoint for faculty details with a dynamic string parameter
        views.FacultyDetail.as_view(),  # View class handling faculty details
        name='faculty_detail'  # Name for reverse URL resolution
    ),
]
