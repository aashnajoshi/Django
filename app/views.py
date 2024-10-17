from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. (request-handler: request -> reponse)
def health_check(request):
    return HttpResponse("Congrats! Django is working")

def greet(request):
    return render(request, 'welcome.html', {'name': 'Qwerty'})

def user_data(request):
    dummy_data = {
        'users': [
            {'name': 'Qwerty', 'age':12},
            {'name': 'Asdfg', 'age': 23},
            {'name': 'Zxcvb', 'age': 34},
            {'name': 'Poiuy', 'age': 43},
            {'name': 'Lkjhg', 'age': 21}]}
    return render(request, 'welcome.html', {'info': dummy_data})