from django.urls import path
from . import views

urlpatterns = [
    path('add-department/', views.AddDepartment.as_view(), name='add_department'),
    path('add-batch/', views.AddBatch.as_view(), name='add_batch'),
    path('add-section/', views.AddSection.as_view(), name='add_section'),
    path('add-semester/', views.AddSemester.as_view(), name='add_semester'),
    path('add-course-to-semester/', views.AddCourseToSemester.as_view(),
         name='add_course_to_semester'),
    path('add-sections-to-semester/', views.AddSectionsToSemester.as_view(),
         name='add_sections_to_semester'),
]
