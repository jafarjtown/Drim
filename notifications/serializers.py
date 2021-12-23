
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Notification
class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            'message',
        ]
class NotificationViewSet(ModelViewSet):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

    def get_queryset(self):
        return self.request.user.received_notification.all().order_by('-created_at')[:5]