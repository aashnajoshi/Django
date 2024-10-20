from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#URL Configurations:
urlpatterns = [
    path('', views.health_check),
    path('greet/', views.greet),
    path('data/', views.user_data),
    path('form/', views.input_form_data, name='form'),
    path('info/', views.form_data),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)