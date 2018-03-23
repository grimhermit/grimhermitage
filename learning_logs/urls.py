"""Определяет схемы URL для learning_logs."""


from django.urls import path

from . import views

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Вывод всех тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # URL формы создания новой темы
    path('new_topic/', views.new_topic, name='new_topic'),
    # URL формы создания новой записи
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Страница для редактирования записи
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]