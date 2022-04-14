from django.urls import path
from . import views

app_name = 'friends'
# from rest_framework import routers
# from .serializers import F
# router = routers.DefaultRouter()

# router.register('activities', )

urlpatterns = [
    path('', views.Followers, name='index'),
    path('request', views.RequestFriends, name='request_friends'),
    path('follow/<slug:pk>', views.Follow, name='follow'),
    path('unfollow/<slug:pk>', views.unFollow, name='unfollow'),
]
