from django.urls import path  # Importing path for URL routing
from . import views  # Importing views to connect URLs to view classes

# Define URL patterns for course-related endpoints
create_course_url: str = 'create-course/'  # URL for creating a course
course_list_url: str = 'courses/'  # URL for listing all courses
# URL for retrieving a specific course by ID
course_detail_url: str = 'course/<str:id>/'

# Define URL patterns for module-related endpoints
create_module_url: str = 'create-module/'  # URL for creating a module
module_list_url: str = 'modules/'  # URL for listing all modules
# URL for retrieving a specific module by ID
module_detail_url: str = 'module/<str:id>/'

# Define URL patterns for lecture-related endpoints
create_lecture_url: str = 'create-lecture/'  # URL for creating a lecture
lecture_list_url: str = 'lectures/'  # URL for listing all lectures
# URL for retrieving a specific lecture by ID
lecture_detail_url: str = 'lecture/<str:id>/'

# URL patterns list
urlpatterns: list[path] = [
    # Course-related URLs
    path(create_course_url, views.CreateCourse.as_view(),
         name='create_course'),  # Create course endpoint
    path(course_list_url, views.CourseList.as_view(),
         name='course_list'),  # List courses endpoint
    path(course_detail_url, views.CourseDetail.as_view(),
         name='course_detail'),  # Course detail endpoint

    # Module-related URLs
    path(create_module_url, views.CreateModule.as_view(),
         name='create_module'),  # Create module endpoint
    path(module_list_url, views.ModuleList.as_view(),
         name='module_list'),  # List modules endpoint
    path(module_detail_url, views.ModuleDetail.as_view(),
         name='module_detail'),  # Module detail endpoint

    # Lecture-related URLs
    path(create_lecture_url, views.CreateLecture.as_view(),
         name='create_lecture'),  # Create lecture endpoint
    path(lecture_list_url, views.LectureList.as_view(),
         name='lecture_list'),  # List lectures endpoint
    path(lecture_detail_url, views.LectureDetail.as_view(),
         name='lecture_detail'),  # Lecture detail endpoint
]
