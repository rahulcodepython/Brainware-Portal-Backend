from django.urls import path  # Importing path for URL routing
from . import views  # Importing views to link URLs to view classes

# Define URL patterns for class routines
add_class_routine_url: str = 'add-class-routine/'  # URL for adding a class routine
# URL for fetching class routines by section
class_routines_url: str = 'class-routines/<str:section>/'
# URL for fetching a specific class routine by ID
class_routine_url: str = 'class-routine/<str:id>/'

# Define URL patterns for lecture plans
add_lecture_plan_url: str = 'add-lecture-plan/'  # URL for adding a lecture plan
# URL for fetching lecture plans by section and course
lecture_plans_url: str = 'lecture-plans/<str:section>/<str:course>/'
# URL for fetching a specific lecture plan by ID
lecture_plan_url: str = 'lecture-plan/<str:id>/'

# Define URL pattern for attendance registration
# URL for registering attendance
register_attendance_url: str = 'register-attendance/'

# URL patterns list
urlpatterns: list = [
    # Class routine URLs
    path(add_class_routine_url, views.AddClassRoutine.as_view(),
         name='add_class_routine'),  # Add class routine
    path(class_routines_url, views.ClassRoutines.as_view(),
         name='class_routines'),  # Fetch class routines
    path(class_routine_url, views.ClassRoutine.as_view(),
         name='class_routine'),  # Fetch specific class routine

    # Lecture plan URLs
    path(add_lecture_plan_url, views.AddLecturePlan.as_view(),
         name='add_lecture_plan'),  # Add lecture plan
    path(lecture_plans_url, views.LecturePlans.as_view(),
         name='lecture_plans'),  # Fetch lecture plans
    path(lecture_plan_url, views.LecturePlan.as_view(),
         name='lecture_plan'),  # Fetch specific lecture plan

    # Attendance registration URL
    path(register_attendance_url, views.RegisterAttendance.as_view(),
         name='register_attendance'),  # Register attendance
]
