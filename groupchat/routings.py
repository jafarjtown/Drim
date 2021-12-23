from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/groupchat/(?P<room_name>\w+)/$', consumers.GroupChatConsumer.as_asgi()),
    re_path(r'ws/personalchat/(?P<thread_id>\w+)/$', consumers.OneToOneChatConsumer.as_asgi()),
]