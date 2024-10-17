from django.urls import path
from . import views

#URL Configurations:
urlpatterns = [
    path('', views.health_check),
    path('greet/', views.greet),
    path('data/', views.user_data),
    path('form/', views.form_data),
]