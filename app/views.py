from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import FormEntry
from .models import Form

# Create your views here. (request-handler: request -> reponse)
def health_check(request):
    return render(request, 'base.html', context={'title': "Home"})

def greet(request):
    return render(request, 'app/index.html', context={'name': 'Qwerty', 'title': "Greet"})

def user_data(request):
    dummy_data = {
        'users': [
            {'name': 'Qwerty', 'age': 12},
            {'name': 'Asdfg', 'age': 23},
            {'name': 'Zxcvb', 'age': 34},
            {'name': 'Poiuy', 'age': 43},
            {'name': 'Lkjhg', 'age': 21}]}
    return render(request, 'app/index.html', context={'info': dummy_data, 'title': "User Data"})

def input_form_data(request):
    if request.method == 'POST':
        form = FormEntry(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully')
            return redirect('info')
        else:
            messages.error(request, 'Form submission failed')
            form = FormEntry(request.POST, request.FILES)
    else:
        form = FormEntry()
    return render(request, 'app/index.html', context={'form': form, 'title': "Enter Form Data"})

def form_data(request):
    data = Form.objects.all()
    return render(request, 'app/index.html', context={'data': data, 'title': "Form Data"})

def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_list = [email.strip() for email in request.POST.get('recipients').split(',')]
        file_path = request.FILES.get('file_path')  # Optional

        email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        
        if file_path:
            email.attach(file_path.name, file_path.read(), file_path.content_type)
        try:
            email.send()
            messages.success(request, 'Email sent successfully!')
        except Exception as e:
            messages.error(request, f'Error sending email: {e}')
        return redirect('send_email')

    else:
        return render(request, 'app/index.html', context={'mail': True, 'settings': settings, 'title': "Send Email"})