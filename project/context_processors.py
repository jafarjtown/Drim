

from django.db.models.query_utils import Q
from institution.models import Institution
from pages.models import Page
from rest_framework.authtoken.models import Token


def contexts(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if Token.objects.filter(user=request.user).exists():
            token = Token.objects.get(user=request.user)
        else:
            token = Token.objects.create(user=request.user)
        # avatar = user.avatar
        # user_notifications = user.received_notification.only('message')[:5]
        # user_pages = user.pages_followed.only('name')
        # user_groups = user.groups_in.only('name')[:5]
        context['token'] = token
        # context['user_avatar'] = avatar
        # context['user_groups'] = user_groups
        # context['user_pages'] = user_pages
        # context['user_notifications'] = user_notifications

    return context
