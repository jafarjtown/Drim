import json
from django.contrib.auth import authenticate, login
from django.db.models.query_utils import Q
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.serializers import RegisterUserSerializer
from .models import User
from rest_auth.registration.views import RegisterView
# Create your views here.


class RegisterUserView(RegisterView):
    serializer_class = RegisterUserSerializer


@login_required(login_url='account:login')
def Account(request):
    return render(request, 'account/index.html')


def AddAvatar(request):
    return render(request, 'account/avatar.html')


def saveAvatar(request):
    user = request.user
    if request.method == 'POST':
        file = request.FILES['file']
        user.avatar = file
        user.save()
    return redirect('home:home')


def ViewAccount(request, id):
    return render(request, 'account/index.html')


def VerifyEmail(request):
    j = json.loads(request.body)
    email = j['email']
    if User.objects.filter(Q(username=email) | Q(email=email)).exists():
        u = 'http://localhost:8000/static/img/logo/logo.png'
        if User.objects.get(Q(username=email) | Q(email=email)).avatar != '':
            u = User.objects.get(email = email).avatar.url
        return JsonResponse({
            'status': 'good',
            'code': 200,
            'avatar': u
        })
    return JsonResponse({
        'status': 'bad',
        'code': 404
    })


def registerUser(request):
    print(request.body)
    json_data = json.loads(request.body)
    u = json_data['username']
    e = json_data['email']
    f = json_data['first_name']
    l = json_data['last_name']
    p = json_data['password']
    try:
        print(p)
        user = User.objects.create_user(
            username=u, email=e, password=p, first_name=f, last_name=l)
        login(request, user)
        return JsonResponse({
            'status': 'good',
            'code': 200
        })
    except e:
        return HttpResponse(e)

def loginUser(request):
    json_data = json.loads(request.body)
    p = json_data['password']
    e = json_data['email']
    try:
        user = User.objects.get(Q(username=e) | Q(email=e))
        u = authenticate(username=user.username, password=p)
        if u is not None:
            login(request, u)
        return JsonResponse({
            'status': 'good',
            'code': 200,
            'user': u.username
        })
    except:
        return JsonResponse({
            'status': 'bad',
            'code': 404,
        })
        pass