from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Faculty
class FacultySerializer(ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class FacultyViewSet(ModelViewSet):
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()