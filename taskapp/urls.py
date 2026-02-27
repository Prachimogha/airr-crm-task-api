from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/create/', views.create_task, name='task-create'),
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
]