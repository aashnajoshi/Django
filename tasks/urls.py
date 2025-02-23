from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

#URL Configurations:
urlpatterns = [
    path('', health_check),
    path('view/', stream_view),  # Single stream view
    path('multiple/', multiple_stream_view),  # Multiple stream view
    path('checkbox/', checkbox_view),  # Checkbox view
    path('text_utils/', text_utils_view),  # Text Utils view
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)