from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#URL Configurations:
urlpatterns = [
    path('', views.health_check),
    path('greet/', views.greet),
    path('data/', views.user_data),
    path('form/', views.form_data),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)