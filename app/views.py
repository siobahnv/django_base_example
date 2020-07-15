from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html', {})

def example_list(request):
    return render(request, 'app/example_list.html', {})

def person(request):
    return render(request, 'app/person.html', {})