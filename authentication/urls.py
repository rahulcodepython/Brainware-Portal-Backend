from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('add-student/', views.AddStudent.as_view(), name='add_student'),
    path('add-faculty/', views.AddFaculty.as_view(), name='add_faculty'),
]
