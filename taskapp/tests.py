from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task, Category

class TaskModelTest(TestCase):

    def test_task_creation(self):
        user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        category = Category.objects.create(name="Work")

        task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            category=category,
            user=user
        )

        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.category.name, "Work")
        self.assertEqual(task.user.username, "testuser")