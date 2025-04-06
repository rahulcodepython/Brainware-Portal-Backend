from django.urls import path
from . import views

urlpatterns = [
    path('create-course/', views.CreateCourse.as_view(), name='create_course'),
    path('courses/', views.CourseList.as_view(), name='course_list'),
    path('course/<str:id>/', views.CourseDetail.as_view(), name='course_detail'),

    path('create-module/', views.CreateModule.as_view(), name='create_module'),
    path('modules/', views.ModuleList.as_view(), name='module_list'),
    path('module/<str:id>/', views.ModuleDetail.as_view(), name='module_detail'),

    path('create-lecture/', views.CreateLecture.as_view(), name='create_lecture'),
    path('lectures/', views.LectureList.as_view(), name='lecture_list'),
    path('lecture/<str:id>/', views.LectureDetail.as_view(), name='lecture_detail'),
]
