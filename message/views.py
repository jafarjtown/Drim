from accounts.models import Contact, User
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import ChatBox, Message, Thread, UserChatBox
# Create your views here.


def Messenger(request):
    context = {}
    chats = UserChatBox.objects.prefetch_related('chats').select_related('user').get_or_create(user= request.user)[0]
    userchat = request.user.user_chat.chats
    friends = []
    for chat in userchat.all():
        friends.append(chat.friend)
    context['chats'] = chats.chats.all().order_by('-updated')
    return render(request, 'messenger/index.html', context)

def MessengerStartChat(request, uid):
    # thread = Thread.objects.get_or_create(chats__in = )
    friend = User.objects.prefetch_related('followers','followings','activities').get(id = uid)
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
    thread.chats.add(chatbox, friendchatbox)


    return redirect('messenger:message')

def MessengerChat(request, uid):
    context = {}
    user = request.user
    contact = Contact.objects.get(id = uid)
    friend = contact.resipient
    if user.user_chat.chats.filter(friend__resipient = friend).exists():
        user_chats = user.user_chat.chats.get(friend__resipient = friend)
    else:
        user_chats = user.user_chat.chats.create(friend = contact)
    if friend.user_chat.chats.filter(friend__resipient = user).exists():
        friend_chats = friend.user_chat.chats.get(friend__resipient = user)
    elif friend.contacts.filter(resipient = user).exists():
        cs = friend.contacts.get(resipient = user)
        friend_chats = friend.user_chat.chats.create(friend = cs)
    else:
        c = Contact.objects.create(resipient = user)
        friend_chats = friend.user_chat.chats.create(friend = c)
        
    thread_id = user_chats.get_thread_id()
    if thread_id != None:
        thread = Thread.objects.get(id = thread_id)
    else:
        thread = Thread.objects.create()
        thread.chats.add(user_chats, friend_chats)
    context['thread_id'] = thread.id
    context['messages'] = user_chats.messages.all()
    context['friend_unseen'] = friend_chats.unseen_messages.all()
    user_chats.unseen_messages.clear()
    
    # context = {'thread_id': uid}
    # thread = Thread.objects.get(id = uid).chats
    # friendchat = thread.exclude(friend = request.user)
    # id = friendchat[0].friend.id
    # friend = User.objects.prefetch_related('followers','followings','subscribed','activities').get(id = id)
    # user = request.user
    # userchat = user.user_chat.chats.get( friend = friend)
    # userchat.seen()
    # friendchat = friend.user_chat.chats
    # if friendchat.filter(friend = user).exists():
    #     chatbox = friendchat.get( friend = user)
    # else:
    #     chatbox = ChatBox.objects.create( friend = user )
    #     friendchat.add(chatbox)
    # context['messages'] = userchat.messages.all().order_by('created_at')
    # context['userchatId'] = uid
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
