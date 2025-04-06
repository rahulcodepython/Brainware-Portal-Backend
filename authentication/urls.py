from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),

    path('add-student/', views.AddStudent.as_view(), name='add_student'),
    path('students/', views.StudentList.as_view(), name='student_list'),
    path('student/<str:code>/', views.StudentDetail.as_view(), name='student_detail'),

    path('add-faculty/', views.AddFaculty.as_view(), name='add_faculty'),
    path('facultys/', views.FacultyList.as_view(), name='faculty_list'),
    path('faculty/<str:code>/', views.FacultyDetail.as_view(), name='faculty_detail'),
]
