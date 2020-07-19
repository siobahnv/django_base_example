from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from django.forms.models import model_to_dict

from .models import *

def getPersonList():
    example_list = Example.objects.all()
    return example_list

# Create your views here.

# def index(request):
#     example_list = getPersonList()
#     context = {'example_list': example_list}
#     return render(request, 'app/index.html', context)

def home(request):
    example_list = getPersonList()
    context = {'example_list': example_list}
    return render(request, 'app/home.html', context)

def example_list(request):
    example_list = getPersonList()
    context = {'example_list': example_list}
    return render(request, 'app/example_list.html', context)

def person(request, person_id):
    person = get_object_or_404(Example, pk=person_id)
    person_dict = model_to_dict(person)
    example_list = getPersonList()
    context = {
        'person': person_dict,
        'example_list': example_list
        }
    return render(request, 'app/person.html', context)

class ExampleCreate(CreateView):
    model = Example
    fields = '__all__'
    success_url = reverse_lazy('app:home')

class ExampleUpdate(UpdateView):
    model = Example
    fields = '__all__'
    success_url = reverse_lazy('app:home')

class ExampleDelete(DeleteView):
    model = Example
    success_url = reverse_lazy('app:home')