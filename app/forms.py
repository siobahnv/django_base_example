
from django import forms
from django.forms import ModelForm, CharField
from .models import Player, Birdie

class EditPlayerModelForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
    
class EditBirdieModelForm(ModelForm):
    class Meta:
        model = Birdie
        fields = '__all__'