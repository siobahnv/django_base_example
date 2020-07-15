
from django import forms
from django.forms import ModelForm
from .models import Example

class EditExampleModelForm(ModelForm):
    class Meta:
        model = Example
        fields = '__all__'
        exclude = ('tags',)