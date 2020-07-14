from django.shortcuts import render

# Create your views here.
def example_list(request):
    return render(request, 'example_list.html', {})