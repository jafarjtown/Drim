import json
from django.contrib.auth import authenticate, login
from django.db.models.query_utils import Q
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from helpers.utils import _delete_file_
from accounts.serializers import RegisterUserSerializer
from .models import Contact, Student, Teacher, User
from rest_auth.registration.views import RegisterView
# Create your views here.


class RegisterUserView(RegisterView):
    serializer_class = RegisterUserSerializer


def studentAccount(request):
    user = request.user
    Student.objects.get_or_create(parent = user)
    return redirect('account:account')

def tutorAccount(request):
    user = request.user
    Teacher.objects.get_or_create(parent = user)
    return redirect('account:account')

@login_required(login_url='account:login')
def Account(request):
    return render(request, 'account/index.html')

def createContact(request):
    user = request.user
    if request.method == 'POST':
        name = request.POST['name']
        id = request.POST['id']
        user_r = User.objects.get(id = id)
        c = user.contacts.get_or_create(resipient= user_r)[0]
        c.name = name
        c.save()
    return redirect('messenger:message')
def AddAvatar(request):
    return render(request, 'account/avatar.html')


def saveAvatar(request):
    user = request.user
    if request.method == 'POST':
        print(request.FILES)
        if request.FILES.get('avatar') is not None:
            if user.avatar != '':_delete_file_(user.avatar.path)
            user.avatar = request.FILES['avatar']
            user.save()
        if request.FILES.get('cover') is not None:
            if user.cover != '':_delete_file_(user.cover.path)
            user.cover = request.FILES['cover']
            user.save()
    return redirect('account:account')


def ViewAccount(request, id):
    account = User.objects.get(id = id)
    if account == request.user:
        return redirect('account:account')
    return render(request, 'account/view.html',{'account':account})


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
    json_data = json.loads(request.body)
    u = json_data['username']
    e = json_data['email']
    f = json_data['first_name']
    l = json_data['last_name']
    p = json_data['password']
    print(e,p)
    try:
        if User.objects.filter(username = u).exists():
           return JsonResponse({
            'status': 'bad',
            'code': 300,
            'message': 'Username already exists'
            })
        user = User.objects.create_user(
            username=u, email=e, password=p, first_name=f, last_name=l)
        login(request, user)
        return JsonResponse({
            'status': 'good',
            'code': 200
        })
    # except U
    except:
        return JsonResponse({
            'status': 'bad',
            'code': 500
        })

def loginUser(request):
    json_data = json.loads(request.body)
    p = json_data['password']
    e = json_data['email']
    print(e,p)
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
            'code': 500,
        })
        pass