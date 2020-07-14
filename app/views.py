from django.shortcuts import render

# Create your views here.
def example_list(request):
    return render(request, 'app/example_list.html', {})