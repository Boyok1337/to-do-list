from django.test import TestCase, Client
from django.urls import reverse
from to_do_list_app.models import Task


class ToggleCompleteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.task = Task.objects.create(content='Test task', deadline='2022-12-31')

    def test_initial_task_status(self):
        task = Task.objects.get(pk=self.task.pk)
        self.assertFalse(task.done_or_not)

    def test_toggle_task_status(self):
        response = self.client.get(reverse('to_do_list_app:toggle-complete', args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)

    def test_task_status_after_first_toggle(self):
        self.client.get(reverse('to_do_list_app:toggle-complete', args=[self.task.pk]))
        task = Task.objects.get(pk=self.task.pk)
        self.assertTrue(task.done_or_not)

    def test_task_status_after_second_toggle(self):
        self.client.get(reverse('to_do_list_app:toggle-complete', args=[self.task.pk]))
        self.client.get(reverse('to_do_list_app:toggle-complete', args=[self.task.pk]))
        task = Task.objects.get(pk=self.task.pk)
        self.assertFalse(task.done_or_not)
