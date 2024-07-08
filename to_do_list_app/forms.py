from django.contrib.auth.forms import UserCreationForm
from django import forms

from to_do_list_app.models import Task, Tag


class User(UserCreationForm):
    pass


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        max_length=255,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your task here!'}),
        label='Task info'
    )
    deadline = forms.DateField(
        widget=forms.SelectDateWidget(),
        label='Choose a deadline date'
    )

    class Meta:
        model = Task
        fields = '__all__'
