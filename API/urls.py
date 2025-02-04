from django.urls import path
from . import views

#URL Configurations:
urlpatterns = [
    path('', views.getData, name='getData'),
    path('post/', views.postData, name='postData'),
]