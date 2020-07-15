from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('list/', views.example_list, name='example_list'),
]

urlpatterns += [
    path('person/', views.person, name='person'),
]