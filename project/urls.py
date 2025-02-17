from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from app.views import greet
from django.conf import settings
from django.conf.urls.static import static

#URL Configurations:
urlpatterns = [
    path('', greet),
    path('admin/', admin.site.urls),
    path('debug/', include(debug_toolbar.urls)),
    path('app/', include('app.urls')),
    path('tasks/', include('tasks.urls')),
    path('api/', include('API.urls')),
    path('accounts/', include('allauth.urls')),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)