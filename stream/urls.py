from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#URL Configurations:
urlpatterns = [
    path('', views.health_check),
    path('view/', views.stream_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)