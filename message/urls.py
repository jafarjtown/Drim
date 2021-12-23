from django.urls import path
from . import views
from rest_framework import routers
from .serializers import ChatBoxViewSet, MessageViewSet, UserChatBoxViewSet
router = routers.DefaultRouter()

router.register('usersChatBoxs', UserChatBoxViewSet)
router.register('ChatBoxs', ChatBoxViewSet)
router.register('messages', MessageViewSet)

app_name = 'messenger'
urlpatterns = [
    path('', views.Messenger, name='message'),
    path('<slug:uid>/', views.MessengerStartChat, name='start-chat'),
    path('<slug:uid>/chat/', views.MessengerChat, name='chat'),
    path('<slug:uid>/chat/setting/', views.MessengerChatSetting, name='chat-setting'),
    path('<slug:uid>/chat/setting/clear/', views.MessengerClearMessages, name='chat-clear'),
]
