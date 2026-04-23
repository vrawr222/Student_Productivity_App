from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Task
from django.views.generic import UpdateView, DeleteView

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')

class TaskList(ListView):
  model=Task

class TaskDetail(DetailView):
  model=Task

class TaskCreate(CreateView):
  model=Task
  fields=['title','description','complete']
  success_url=reverse_lazy('tasks') #After form is submitted successfully, go to the page named 'tasks'
  #In urls.py:
#path('', TaskList.as_view(), name='tasks')
#So 'tasks' = homepage / task list page.

#Instead of writing a full function like:

#def create_task(request):
 #   ...

#Django gives you CreateView, which already knows how to:

#✅ show a form
#✅ save data to database
#✅ redirect after saving

#You just tell it what model to use, what fields to show, and where to go after saving.