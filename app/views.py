from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import AddTaskForm
from app.models import TaskModel
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

# Create your views here.

def add_task(request):
    if request.method=='POST':
        form=AddTaskForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('show')
    form=AddTaskForm()
    return render(request, './add_task.html', {'form':form})

class add_task_fv(FormView):    # the keyword for accessing the form in front end is 'form'
    form_class = AddTaskForm    # form object
    template_name = 'add_task.html'     # template where the form is shown
    success_url =  '/'   # redirect template on successful form submission

    def form_valid(self, form: Any) -> HttpResponse:    # this function do neccessary works on successful form
        form.save()                                     # form submission i.e. save the form into database
        return super().form_valid(form)

class add_task_cv(CreateView):    # this class handles form.save() on itself
    form_class = AddTaskForm    # form object
    template_name = 'add_task.html'     # template where the form is shown
    success_url =  '/'   # redirect template on successful form submission


def show_tasks(request):
    data=TaskModel.objects.filter(is_completed=False)
    return render(request, './show_tasks.html', {'data':data})

class show_taksks_tv(TemplateView):
    template_name='show_tasks.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data=TaskModel.objects.filter(is_completed=False)
        context = super().get_context_data(**kwargs)
        context = {'data':data}
        return context

class show_tasks_lv(ListView):
    template_name='show_tasks.html'
    model=TaskModel
    context_object_name='data'
    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=False)
    # ordering=['taskTitle']
    

def completed_tasks(request):
    data=TaskModel.objects.filter(is_completed=True)
    return render(request, './completed_tasks.html',{'data':data})

def delete_task(request, id):
    TaskModel.objects.get(pk=id).delete()
    return redirect('show')

class delete_task_dv(DeleteView):
    model=TaskModel
    success_url = '/'

class delete_task_tv(TemplateView):
    template_name='show_tasks.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        # context = super().get_context_data(**kwargs)
        print(kwargs) # receives kwarg from urls.py
        # context.update(kwargs)
        TaskModel.objects.get(pk=kwargs['id']).delete()
    

def completed(request, id):
    print('comleted', id)
    task=TaskModel.objects.get(pk=id)
    task.is_completed=True
    task.save()
    return redirect('completed')

def edit(request, id):
    task=TaskModel.objects.get(pk=id)
    if request.method=='POST':
        form=AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show')
    form=AddTaskForm(instance=task)
    return render(request, './add_task.html', {'form':form})


class edit_uv(UpdateView):
    form_class=AddTaskForm
    success_url ='/'
    model=TaskModel
    template_name = 'add_task.html'