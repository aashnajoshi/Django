from django.urls import path
from . import views

app_name = "main"

#URL Configurations:
urlpatterns = [
    path('', views.greet),
    path('greet/', views.greet),
    path('data/', views.user_data)
]