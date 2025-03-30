from django.urls import path
from . import views

urlpatterns = [
    path('create-course/', views.CreateCourse.as_view(), name='create_course'),
    path('create-module/', views.CreateModule.as_view(), name='create_module'),
    path('create-lecture/', views.CreateLecture.as_view(), name='create_lecture'),
    path('add-module-to-course/', views.AddModuleToCourse.as_view(),
         name='add_module_to_course'),
    path('add-lecture-to-module/', views.AddLectureToModule.as_view(),
         name='add_lecture_to_module'),
]
