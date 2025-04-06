from django.urls import path
from . import views

urlpatterns = [
    path('add-department/', views.AddDepartment.as_view(), name='add_department'),
    path('departments/', views.Departments.as_view(), name='departments'),
    path('department/<str:id>/', views.Department.as_view(), name='department'),

    path('add-batch/', views.AddBatch.as_view(), name='add_batch'),
    path('batches/', views.Batches.as_view(), name='batches'),
    path('batch/<str:id>/', views.Batch.as_view(), name='batch'),

    path('add-section/', views.AddSection.as_view(), name='add_section'),
    path('sections/', views.Sections.as_view(), name='sections'),
    path('section/<str:id>/', views.Section.as_view(), name='section'),

    path('add-semester/', views.AddSemester.as_view(), name='add_semester'),
    path('semesters/', views.Semesters.as_view(), name='semesters'),
    path('semester/<str:id>/', views.Semester.as_view(), name='semester'),

    path('semester-course-faculty/<str:semester>/<str:course>/',
         views.SemesterCourseFaculty.as_view(), name='semester_course_faculty'),
]
