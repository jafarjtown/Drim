from django.urls import path
from .views import GroupJoinLeave, GroupMakeAdmin, GroupMembers, GroupPost, GroupPrivacy, GroupSetting, GroupView, Groups
from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers
from .serializers import GroupViewSet
router = routers.DefaultRouter()

router.register('groups', GroupViewSet)

app_name = 'group'

urlpatterns = [
    path('', Groups, name='groups'),
    path('<slug:gid>/new-posts', csrf_exempt(GroupPost) , name='create_post'),
    path('<slug:gid>/', GroupView , name='group'),
    path('<slug:gid>/setting/', GroupSetting, name='group-setting'),
    path('<slug:gid>/privacy/', GroupPrivacy, name='group-private'),
    path('<slug:gid>/members/', GroupMembers, name='group-members'),
    path('<slug:gid>/make-admin/<slug:uid>/', GroupMakeAdmin, name='group-make-admin'),
    path('<slug:gid>/join-or-leave/', GroupJoinLeave, name='group-join-or-leave'),

]
