from django.http.response import JsonResponse
from django.shortcuts import render
from accounts.models import User
from django.db.models.query import Q
from notifications.notifcations import FriendRequestNotification
# Create your views here.


def Followers(request):
    user = request.user
    friends = User.objects.all()
    f = []
    for friend in friends.all():
        if friend not in user.followings.all():
            f.append(friend)
    context = {
        'suggestions': f
    }
    return render(request, 'friends/index.html', context)

def RequestFriends(request):
    return render(request, 'friends/s_request.html')

def Follow(request, pk):
    to = User.objects.get(id=pk)
    sender = request.user
    sender.followings.add(to)
    to.followers.add(sender)
    FriendRequestNotification(to, sender, 'follow').send()
    return JsonResponse({
        'response': 'successfull',
        'friend': f'{to.first_name} {to.last_name}'
    })

def unFollow(request, pk):
    to = User.objects.get(id=pk)
    sender = request.user
    sender.followings.remove(to)
    to.followers.remove(sender)
    return JsonResponse({
        'response': 'successfull',
        'friend': to.username
    })