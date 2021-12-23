from accounts.models import User
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import ChatBox, Message, Thread, UserChatBox
# Create your views here.


def Messenger(request):
    context = {}
    try:
        chats = UserChatBox.objects.prefetch_related('chats').select_related('user').get(user= request.user)
    except Exception as e:
        chats = UserChatBox.objects.create(user = request.user)
    userchat = request.user.user_chat.chats
    friends = []
    for chat in userchat.all():
        friends.append(chat.friend)
    context['chats'] = chats.chats.all().order_by('-updated_at')
    context['friends'] = friends
    return render(request, 'messenger/index.html', context)

def MessengerStartChat(request, uid):
    # thread = Thread.objects.get_or_create(chats__in = )
    friend = User.objects.prefetch_related('followers','followings','subscribed','activities').get(id = uid)
    user = request.user
    userchat = UserChatBox.objects.get_or_create(user = user)[0].chats

    # friendchat = friend.user_chat.chats
    friends = []
    for chat in userchat.all():
        friends.append(chat.friend)
    if friend in friends:
        chatbox = userchat.get(friend = friend)
        userchat.remove(chatbox)
        chatbox.delete()
    else:
        chatbox = ChatBox.objects.create( friend = friend )
        userchat.add(chatbox)
    # userchat.save()
    # if Thread.objects.filter(Q(chats = chatbox )).exists():
    #     print('yes')
    # else:
    if UserChatBox.objects.get_or_create(user = friend)[0].chats.filter( friend = user).exists():
        friendchatbox = friend.user_chat.chats.get( friend = user)
    else:
        friendchatbox = friend.user_chat.chats.create( friend = user)
    thread = Thread.objects.create()
    print(chatbox)
    thread.chats.add(chatbox, friendchatbox)


    return redirect('messenger:message')

def MessengerChat(request, uid):
    context = {'thread_id': uid}
    thread = Thread.objects.get(id = uid).chats
    friendchat = thread.exclude(friend = request.user)
    id = friendchat[0].friend.id
    friend = User.objects.prefetch_related('followers','followings','subscribed','activities').get(id = id)
    user = request.user
    userchat = user.user_chat.chats.get( friend = friend)
    userchat.seen()
    friendchat = friend.user_chat.chats
    if friendchat.filter(friend = user).exists():
        chatbox = friendchat.get( friend = user)
    else:
        chatbox = ChatBox.objects.create( friend = user )
        friendchat.add(chatbox)
    context['messages'] = userchat.messages.all().order_by('created_at')
    context['userchatId'] = uid
    return render(request, 'messenger/messenger.chat.html', context)

def MessengerChatSetting(request, uid):
    context = {}
    context['uid'] = uid
    return render(request, 'messenger/messenger.chat.settings.html', context)

def MessengerClearMessages(request, uid):
    thread = Thread.objects.get(id = uid).chats
    friendchat = thread.exclude(friend = request.user)
    id = friendchat[0].friend.id
    friend = User.objects.prefetch_related('followers','followings','subscribed','activities').get(id = id)
    user = request.user
    userchat = user.user_chat.chats.get( friend = friend)
    userchat.messages.clear()
    return redirect('messenger:chat-setting', uid )