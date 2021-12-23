from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Institution
class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

class InstitutionViewSet(ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()