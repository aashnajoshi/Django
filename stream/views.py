from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def health_check(request):
    return HttpResponse("<center><h2>Congrats! Django is working</h2></center>")