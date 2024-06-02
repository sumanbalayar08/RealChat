from django.urls import path, include
from Chatter.user import ChatUser

# the empty string routes to ChatConsumer, which manages the chat functionality.
websocket_urlpatterns = [
    path("", ChatUser.as_asgi()),
]