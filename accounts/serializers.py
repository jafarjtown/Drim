from django.db.models.query_utils import Q
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from .models import User

class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name', 'avatar', 'is_student', 'is_teacher']


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerialzer

    def get_queryset(self):
        user = self.request.user
        users = User.objects.filter(Q(faculty = user.faculty)|Q(department = user.department)).exclude(username = user.username)
        not_friends = []
        for u in users.all():
            if u not in user.followings.all():
                not_friends.append(u)
        
        return not_friends
