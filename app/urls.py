from tinymce import urls as tinymce_urls
from django.urls import path, include
from . import views

#URL Configurations:
urlpatterns = [
    path('', views.health_check),
    path('greet/', views.greet, name='greet'),
    path('data/', views.user_data, name='data'),
    path('form/', views.input_form_data, name='form'),
    path('info/', views.form_data, name='info'),
    path('tinymce/', include(tinymce_urls)),
    path('send_email/', views.send_email, name='send_email'),]