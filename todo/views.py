from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import todolist


class index(ListView):
    model=todolist
    context_object_name='todo'
    ordering=['-dateposted']



class createtodo(CreateView):
    model=todolist
    fields=['todoitem','done']
    context_object_name='todo'

class updatetodo(UpdateView):
    model=todolist
    fields=['todoitem','done']

class deletetodo(DeleteView):
    model=todolist
    template_name='todo/delete.html'
    success_url='/'
    
    
