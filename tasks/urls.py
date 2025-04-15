from django.urls import path
from .views import *

#URL Configurations:
urlpatterns = [
    path('', health_check, name='health_check'),  # Health check view
    path('view/', stream_view, name='stream_view'),  # Single stream view
    path('multiple/', multiple_stream_view, name='multiple_stream_view'),  # Multiple stream view
    path('checkbox/', checkbox_view, name='checkbox_view'),  # Checkbox view
    path('text_utils/', text_utils_view, name='text_utils_view'),  # Text Utils view
]