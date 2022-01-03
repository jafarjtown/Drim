from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from accounts.serializers import UserSerializer

from posts.models import Post
from .models import Institution
class InstitutionSerializer(ModelSerializer):
    class Meta:
        model = Institution
        exclude= ['blogs']

class InstitutionViewSet(ModelViewSet):
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()


class instSetSerializerPost(ModelSerializer):
    class Meta:
        model = Institution
        fields = ['name','logo', 'id','verified']

class PostSerializer(ModelSerializer):
    author = UserSerializer()
    institution = instSetSerializerPost(many=True)
    class Meta:
        model = Post
        fields = '__all__'
        depth = 3


class InstitutionBlogsSerializer(ModelSerializer):
    blogs = PostSerializer(many=True)
    class Meta:
        model = Institution
        fields = ['blogs']
        
        depth = 3

class InstitutionBlogsViewSet(ModelViewSet):
    serializer_class = InstitutionBlogsSerializer
    queryset = Institution.objects.all()
    