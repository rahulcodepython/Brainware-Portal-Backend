from django.urls import path
from . import views

urlpatterns = [
    path('add-class-routine/', views.AddClassRoutine.as_view(),
         name='add_class_routine'),
    # path('update-class-routine/', UpdateClassRoutine.as_view(), name='update_class_routine'),
    # path('delete-class-routine/', DeleteClassRoutine.as_view(), name='delete_class_routine'),
    # path('get-class-routines/', GetClassRoutines.as_view(), name='get_class_routines'),
    # path('get-class-routine/<int:pk>/', views.GetClassRoutine.as_view(),
    #      name='get_class_routine'),
    path('add-lecture-plan/', views.AddLecturePlan.as_view(),
         name='add_lecture_plan'),
]
