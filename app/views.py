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
            {'name': 'Alice', 'age':12},
            {'name': 'Bob', 'age': 23},
            {'name': 'Charlie', 'age': 34},
            {'name': 'Diana', 'age': 43},
            {'name': 'Eve', 'age': 21}
        ]
    }
    return render(request, 'welcome.html', {'info': dummy_data})