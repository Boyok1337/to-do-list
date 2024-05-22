from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from to_do_list_app.forms import TaskForm
from to_do_list_app.models import Task, Tag


def home(request):
    return render(request, 'to_do_list_app/task_list.html')


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 6


class TaskDetailView(generic.DetailView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('to_do_list_app:task-list')


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'to_do_list_app/task_confirm_delete.html'
    success_url = reverse_lazy('to_do_list_app:task-list')


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('to_do_list_app:task', kwargs={'pk': pk})


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 6


class TagCreateView(generic.CreateView):
    model = Tag
    fields = '__all__'
    template_name = 'to_do_list_app/tag_form.html'
    success_url = reverse_lazy('to_do_list_app:tag-list')


class TagDetailView(generic.DetailView):
    model = Tag


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'to_do_list_app/tag_confirm_delete.html'
    success_url = reverse_lazy('to_do_list_app:tag-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = '__all__'

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse_lazy('to_do_list_app:tag-detail', kwargs={'pk': pk})


def toggle_complete(request, pk):
    task = Task.objects.get(pk=pk)
    task.done_or_not = not task.done_or_not
    task.save()
    return redirect('to_do_list_app:task-list')
