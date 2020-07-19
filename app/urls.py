from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('list/', views.example_list, name='example_list'),
]

urlpatterns += [
    path('person/<int:person_id>', views.person, name='person'),
]

urlpatterns += [  
    path('create/', views.ExampleCreate.as_view(), name='example_create'),
    path('<int:pk>/update/', views.ExampleUpdate.as_view(), name='example_update'),
    path('<int:pk>/delete/', views.ExampleDelete.as_view(), name='example_delete'),
]

# Trying to get CSS to work locally
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
