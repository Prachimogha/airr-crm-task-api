from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='task-list-create'),  # GET + POST
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),    # GET/PUT/DELETE for single task
]