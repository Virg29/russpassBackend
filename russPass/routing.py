from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import groupNotifier.routing
import eventNotifier.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            groupNotifier.routing.websocket_urlpatterns
        )
    ),
    'websocket': AuthMiddlewareStack(
        URLRouter(
        	eventNotifier.routing.websocket_urlpatterns
        )
    ),
})