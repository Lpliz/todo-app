from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import ToDoTask

# Create your tests here.
# Test Cases
class ToDoTaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {'title': 'Test Task', 'description': 'Test Description'}
        self.task = ToDoTask.objects.create(**self.task_data)

    def test_get_tasks(self):
        response = self.client.get('/todo/display')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_create_task(self):
        response = self.client.post('/todo/add', self.task_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task_detail(self):
        response = self.client.get(f'/todo/display/{self.task.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        updated_data = {'title': 'Updated Task', 'description': 'Updated Description'}
        response = self.client.put(f'/todo/edit/{self.task.id}', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(f'/todo/delete/{self.task.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_all_tasks(self):
        response = self.client.delete('/todo/deleteAll')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)