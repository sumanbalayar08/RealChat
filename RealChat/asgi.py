"""
ASGI config for RealChat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import Chatter.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RealChat.settings')

# Define the ASGI application
application = ProtocolTypeRouter({
    # For handling HTTP requests, use the default Django ASGI application
    "http": get_asgi_application(),
    # For handling WebSocket connections, use the AuthMiddlewareStack to handle authentication
    "websocket": AuthMiddlewareStack(
        # Use the URLRouter to route WebSocket connections to the appropriate consumers
        URLRouter(
            Chatter.routing.websocket_urlpatterns
        )
    ),
})
