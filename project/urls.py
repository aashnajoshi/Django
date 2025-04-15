import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from app.views import greet

#URL Configurations:
urlpatterns = [
    path('', greet, name='greet'),
    path('admin/', admin.site.urls),
    path('debug/', include(debug_toolbar.urls)),
    path('accounts/', include('allauth.urls')),
    path('app/', include('app.urls')),
    path('tasks/', include('tasks.urls')),
    path('api/', include('API.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)