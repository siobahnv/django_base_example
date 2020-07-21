from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from django.forms.models import model_to_dict

from .models import *

def getPersonList():
    player_list = Player.objects.all()
    return player_list

def getBirdieList():
    birdie_list = Birdie.objects.all()
    return birdie_list

# Create your views here.

# def index(request):
#     example_list = getPersonList()
#     context = {'example_list': example_list}
#     return render(request, 'app/index.html', context)

def home(request):
    player_list = getPersonList()
    context = {'player_list': player_list}
    return render(request, 'app/home.html', context)

def player_list(request):
    player_list = getPersonList()
    birdie_list = getBirdieList()
    context = {
        'player_list': player_list, # Necessary for nav in base.html
        'birdie_list': birdie_list
        }
    return render(request, 'app/player_list.html', context)

def birdie_list(request):
    player_list = getPersonList()
    birdie_list = getBirdieList()
    context = {
        'player_list': player_list, # Necessary for nav in base.html
        'birdie_list': birdie_list
        }
    return render(request, 'app/player_list.html', context)

def person(request, person_id):
    person = get_object_or_404(Player, pk=person_id)
    person_dict = model_to_dict(person)
    player_list = getPersonList()
    context = {
        'person': person_dict,
        'player_list': player_list # Necessary for nav in base.html
        }
    return render(request, 'app/person.html', context)

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'
    success_url = reverse_lazy('app:home')

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'
    success_url = reverse_lazy('app:home')

class PlayerDelete(DeleteView):
    model = Player
    success_url = reverse_lazy('app:home')

class BirdieCreate(CreateView):
    model = Birdie
    fields = '__all__'
    success_url = reverse_lazy('app:home')

class BirdieUpdate(UpdateView):
    model = Birdie
    fields = '__all__'
    success_url = reverse_lazy('app:home')

class BirdieDelete(DeleteView):
    model = Birdie
    success_url = reverse_lazy('app:home')