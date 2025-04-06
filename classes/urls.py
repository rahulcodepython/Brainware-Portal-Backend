from django.urls import path
from . import views

urlpatterns = [
    path('add-class-routine/', views.AddClassRoutine.as_view(),
         name='add_class_routine'),
    path('class-routines/<str:section>/', views.ClassRoutines.as_view(),
         name='class_routines'),
    path('class-routine/<str:id>/', views.ClassRoutine.as_view(),
         name='class_routine'),

    path('add-lecture-plan/', views.AddLecturePlan.as_view(),
         name='add_lecture_plan'),
    path('lecture-plans/<str:section>/<str:course>/', views.LecturePlans.as_view(),
         name='lecture_plans'),
    path('lecture-plan/<str:id>/', views.LecturePlan.as_view(),
         name='lecture_plan'),

    path('register-attendance/', views.RegisterAttendance.as_view(),
         name='register_attendance'),
]
