from django.shortcuts import render

# Create your views here.

def Index(request, room_name):
    context = {}
    context['room_name'] = room_name
    return render(request, 'groupchat/index.html', context)