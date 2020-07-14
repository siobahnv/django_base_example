from django.urls import path
from . import views

urlpatterns = [
    path('', views.example_list, name='example_list'),
]