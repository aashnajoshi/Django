from django.urls import path
from .views import *

#URL Configurations:
urlpatterns = [
    path('', getData, name='getData'),
    path('post/', postData, name='postData'),
]