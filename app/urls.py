from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.example_list, name='example_list'),
    path('home/', views.home, name='home'),
]