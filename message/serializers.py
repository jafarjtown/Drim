from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Message, UserChatBox, ChatBox
class UserChatBoxSerializer(ModelSerializer):
    class Meta:
        model = UserChatBox
        fields = '__all__'

class UserChatBoxViewSet(ModelViewSet):
    serializer_class = UserChatBoxSerializer
    queryset = UserChatBox.objects.all()


class ChatBoxSerializer(ModelSerializer):
    class Meta:
        model = ChatBox
        fields = '__all__'

class ChatBoxViewSet(ModelViewSet):
    serializer_class = ChatBoxSerializer
    queryset = ChatBox.objects.all()


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()