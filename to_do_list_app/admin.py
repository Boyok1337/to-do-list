from django.contrib import admin
from .models import Task, Tag, User

admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(User)
