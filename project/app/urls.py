from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/create/', views.project_create, name='project_create'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/<int:pk>/task/add/', views.task_create, name='task_create'),
    path('task/<int:pk>/status/', views.task_update_status, name='task_update_status'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]