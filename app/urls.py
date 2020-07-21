from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('players/', views.player_list, name='player_list'),
    path('list/', views.birdie_list, name='birdie_list')
]

urlpatterns += [
    path('person/<int:person_id>', views.person, name='person'),
]

urlpatterns += [  
    path('create/', views.BirdieCreate.as_view(), name='birdie_create'),
    path('<int:pk>/update/', views.BirdieUpdate.as_view(), name='birdie_update'),
    path('<int:pk>/delete/', views.BirdieDelete.as_view(), name='birdie_delete'),
]

# Trying to get CSS to work locally
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
