from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

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