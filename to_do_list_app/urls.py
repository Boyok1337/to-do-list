from django.urls import path

from to_do_list_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/', views.TaskListView.as_view(), name='task-list'),
    path('task/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('task/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tags/', views.TagListView.as_view(), name='tag-list'),
    path('tags/create/', views.TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/', views.TagDetailView.as_view(), name='tag-detail'),
    path('tags/<int:pk>/delete/', views.TagDeleteView.as_view(), name='tag-delete'),
    path('tags/<int:pk>/update/', views.TagUpdateView.as_view(), name='tag-update'),
    path('toggle-complete/<int:pk>/', views.toggle_complete, name='toggle-complete'),
]

app_name = 'to_do_list_app'
