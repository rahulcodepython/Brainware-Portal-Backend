from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard_template'),
    path('login/', views.login, name='login_template'),
    path('profile/', views.profile, name='profile_template'),
    path('login-user/', views.loginUser, name='login')
]
