from django.shortcuts import render
from django.http import HttpResponse
from .models import form

# Create your views here. (request-handler: request -> reponse)
def health_check(request):
    return HttpResponse("Congrats! Django is working")

def greet(request):
    return render(request, 'index.html', {'name': 'Qwerty'})

def user_data(request):
    dummy_data = {
        'users': [
            {'name': 'Qwerty', 'age':12},
            {'name': 'Asdfg', 'age': 23},
            {'name': 'Zxcvb', 'age': 34},
            {'name': 'Poiuy', 'age': 43},
            {'name': 'Lkjhg', 'age': 21}]}
    return render(request, 'index.html', {'info': dummy_data})

def form_data(request):
    data = form.objects.all()
    return render(request, 'index.html', {'data': data})