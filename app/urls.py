from django.urls import path, include
from .views import *

#URL Configurations:
app_name = 'app'
urlpatterns = [
    path('', health_check, name='home'),
    path('greet/', greet, name='greet'),
    path('data/', user_data, name='data'),
    path('form/', input_form_data, name='form'),
    path('info/', form_data, name='info'),
    path('send_email/', send_email, name='send_email'),]