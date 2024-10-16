from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. (request-handler: request -> reponse)

def greet(request):
    # return HttpResponse("Hey!")
    return render(request, 'welcome.html', {'name': 'Qwerty'})