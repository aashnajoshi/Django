from django.shortcuts import render
from django.http import HttpResponse
from .models import form

# Create your views here. (request-handler: request -> reponse)
def health_check(request):
    return HttpResponse("<center>Congrats! Django is working</center>") # Usage of HTTP response for Static

def greet(request):
    return render(request, 'index.html', context = {'name': 'Qwerty'}) # Usage of render function for Static

def user_data(request): # Usage of render function for Partially Dynamic (data from views.py file)
    dummy_data = {
        'users': [
            {'name': 'Qwerty', 'age':12},
            {'name': 'Asdfg', 'age': 23},
            {'name': 'Zxcvb', 'age': 34},
            {'name': 'Poiuy', 'age': 43},
            {'name': 'Lkjhg', 'age': 21}]}
    return render(request, 'index.html', context = {'info': dummy_data})

def form_data(request): # Usage of render function for Dynamic (data from database)
    data = form.objects.all()
    return render(request, 'index.html', context = {'data': data})