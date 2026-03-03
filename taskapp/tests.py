from django.test import TestCase
from .models import Task, Category

class TaskModelTest(TestCase):

    def test_task_creation(self):
        category = Category.objects.create(name="Work")

        task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            category=category
        )

        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.category.name, "Work")