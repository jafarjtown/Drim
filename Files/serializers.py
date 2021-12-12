from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import File
class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class FileViewSet(ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()