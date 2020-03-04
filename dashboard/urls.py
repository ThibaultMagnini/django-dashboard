from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.landing, name='landing'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login-user'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/logout.html'), name='logout-user'),
    path('home/', views.home, name='home'),
]
