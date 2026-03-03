from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Category

class TaskAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="apiuser",
            password="testpass123"
        )
        self.category = Category.objects.create(name="Work")
        self.client.login(username="apiuser", password="testpass123")

    def test_create_task_api(self):
        url = reverse("task-list")  # make sure your router name matches
        data = {
            "title": "API Task",
            "description": "API Test",
            "category": self.category.id
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)