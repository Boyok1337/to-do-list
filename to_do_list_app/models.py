from django.contrib.auth.models import AbstractUser, Group, Permission

from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done_or_not = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', related_name='tasks')

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    tasks = models.ManyToManyField(Task, related_name='users', blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set')
