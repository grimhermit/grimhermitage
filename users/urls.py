"""Определяет схемы URL для users"""
from django.contrib.auth.views import login

from django.urls import path

from . import views

urlpatterns = [
    # Страница входа пользователей
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    # Страница выхода пользователей
    path('logout/', views.logout_view, name="logout"),
    # Страница регистрации пользователей
    path('register/', views.register, name="register"),
]