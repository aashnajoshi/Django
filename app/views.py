from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FormEntry
from .forms import FormEntryForm  

# Create your views here. (request-handler: request -> reponse)
def health_check(request):
    return HttpResponse("<center>Congrats! Django is working</center>")

def greet(request):
    return render(request, 'index.html', context={'name': 'Qwerty'})

def user_data(request):
    dummy_data = {
        'users': [
            {'name': 'Qwerty', 'age': 12},
            {'name': 'Asdfg', 'age': 23},
            {'name': 'Zxcvb', 'age': 34},
            {'name': 'Poiuy', 'age': 43},
            {'name': 'Lkjhg', 'age': 21}
        ]}
    return render(request, 'index.html', context={'info': dummy_data})

def input_form_data(request):
    if request.method == 'POST':
        form = FormEntryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('form')
    else:
        form = FormEntryForm()
    return render(request, 'index.html', {'form': form})

def form_data(request):
    data = FormEntry.objects.all()
    return render(request, 'index.html', context={'data': data})