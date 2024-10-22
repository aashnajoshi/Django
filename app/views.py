from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Form
from .forms import FormEntry 

# Create your views here. (request-handler: request -> reponse)
def health_check(request):
    return HttpResponse('''
    <center><h2>Congrats! Django is working</h2></center>
    <p> The links you can visit are: 
    <ul style ="none">
        <li><a href="/app/greet">Greet</a></li>
        <li><a href="/app/data">User Data</a></li>
        <li><a href="/app/form">Input Form Data</a></li>
        <li><a href="/app/info">Form Data</a></li>
        <li><a href="/stream/">Stream</a></li>
    </ul>    
    ''')

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
        form = FormEntry(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully')
            return redirect('form')
        else:
            messages.error(request, 'Form submission failed')
    else:
        form = FormEntry()
    return render(request, 'index.html', context={'form': form})

def form_data(request):
    data = Form.objects.all()
    return render(request, 'index.html', context={'data': data})