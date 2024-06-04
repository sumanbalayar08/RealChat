from django.urls import re_path
from . import consumers

# Define WebSocket URL patterns
websocket_urlpatterns = [
    # Route WebSocket connections to the ChatConsumer consumer, capturing the username from the URL
    re_path(r'ws/chat/(?P<username>\w+)/$', consumers.ChatConsumer.as_asgi()),
]
