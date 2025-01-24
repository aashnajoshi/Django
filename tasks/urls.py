from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#URL Configurations:
urlpatterns = [
    path('', views.health_check),
    path('view/', views.stream_view),  # Single stream view
    path('multiple/', views.multiple_stream_view),  # Multiple stream view
    path('checkbox/', views.checkbox_view),  # Checkbox view
    path('text_utils/', views.text_utils_view),  # Text Utils view
    path('payment/', views.payment_view),  # Payment view
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)