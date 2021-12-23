from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Page
class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class PageViewSet(ModelViewSet):
    serializer_class = PageSerializer
    queryset = Page.objects.all()