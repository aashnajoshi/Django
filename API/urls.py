from django.urls import path
from .views import *

#URL Configurations:
app_name = 'API'
urlpatterns = [
    path('', getData, name='getData'),
    path('post/', postData, name='postData'),
]