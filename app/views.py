from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
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

def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_list = [email.strip() for email in request.POST.get('recipients').split(',')]
        file_path = request.FILES.get('file_path')  # Optional

        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        
        if file_path:
            email.attach(file_path.name, file_path.read(), file_path.content_type)

        if email.send():
            messages.success(request, 'Mail sent successfully!')
        else:
            messages.error(request, 'Failed to send mail. Please try again.')

        return redirect('send_email')
    else:
        return render(request, 'index.html', context={'mail': 'mail'})