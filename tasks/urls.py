from django.urls import path
from .views import *

#URL Configurations:
app_name = 'tasks'
urlpatterns = [
    path('', health_check, name='home'),  # Health check view
    path('view/', stream_view, name='stream'),  # Single stream view
    path('multiple/', multiple_stream_view, name='streams'),  # Multiple stream view
    path('checkbox/', checkbox_view, name='checkbox'),  # Checkbox view
    path('text_utils/', text_utils_view, name='text_utils'),  # Text Utils view
]