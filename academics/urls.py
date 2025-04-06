from django.urls import path  # Importing path for URL routing
from . import views  # Importing views from the current package

# Define URL patterns for department-related views
add_department_url: str = 'add-department/'
departments_url: str = 'departments/'
department_detail_url: str = 'department/<str:id>/'

# Define URL patterns for batch-related views
add_batch_url: str = 'add-batch/'
batches_url: str = 'batches/'
batch_detail_url: str = 'batch/<str:id>/'

# Define URL patterns for section-related views
add_section_url: str = 'add-section/'
sections_url: str = 'sections/'
section_detail_url: str = 'section/<str:id>/'

# Define URL patterns for semester-related views
add_semester_url: str = 'add-semester/'
semesters_url: str = 'semesters/'
semester_detail_url: str = 'semester/<str:id>/'

# Define URL pattern for semester-course-faculty view
semester_course_faculty_url: str = 'semester-course-faculty/<str:semester>/<str:course>/'

# URL patterns list
urlpatterns: list = [
    # Department-related URLs
    path(add_department_url, views.AddDepartment.as_view(),
         name='add_department'),  # Add department
    path(departments_url, views.Departments.as_view(),
         name='departments'),  # List all departments
    path(department_detail_url, views.Department.as_view(),
         name='department'),  # Department details by ID

    # Batch-related URLs
    path(add_batch_url, views.AddBatch.as_view(), name='add_batch'),  # Add batch
    path(batches_url, views.Batches.as_view(),
         name='batches'),  # List all batches
    path(batch_detail_url, views.Batch.as_view(),
         name='batch'),  # Batch details by ID

    # Section-related URLs
    path(add_section_url, views.AddSection.as_view(),
         name='add_section'),  # Add section
    path(sections_url, views.Sections.as_view(),
         name='sections'),  # List all sections
    path(section_detail_url, views.Section.as_view(),
         name='section'),  # Section details by ID

    # Semester-related URLs
    path(add_semester_url, views.AddSemester.as_view(),
         name='add_semester'),  # Add semester
    path(semesters_url, views.Semesters.as_view(),
         name='semesters'),  # List all semesters
    path(semester_detail_url, views.Semester.as_view(),
         name='semester'),  # Semester details by ID

    # Semester-course-faculty URL
    path(semester_course_faculty_url, views.SemesterCourseFaculty.as_view(),
         name='semester_course_faculty'),  # Faculty for a course in a semester
]
