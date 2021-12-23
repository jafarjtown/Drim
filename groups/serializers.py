from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Group
class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.only('name', 'description')

    def get_queryset(self):
        return self.request.user.groups_in.all()