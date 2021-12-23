from django.contrib.auth import login
from django.shortcuts import render 
from django.contrib.auth.hashers import check_password
# Create your views here.


def UserSetting(request):
    return render(request, 'user_settings/index.html')

def UserPersonalInfo(request):
    context = {}
    if request.method == 'POST':
        password = request.POST['password']
        currentpassword = request.user.password
        match = check_password(password, currentpassword)
        if match:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
            message = f'Successfully save changed'
        else:
            message = f'password is incorrect'
        context['message'] = message
    return render(request, 'user_settings/personalInfo.html', context)



def UserInstitution(request):
    if request.method == 'POST':
       pass
    return render(request, 'user_settings/institutions.html')

def UserActivities(request):
    if request.method == 'POST':
       pass
    return render(request, 'user_settings/activities.html')

def UserChangePAssword(request):
    context = {}
    if request.method == 'POST':
        user = request.user
        new_password = request.POST['new_password']
        old_password = request.POST['old_password']
        match_password = check_password(old_password, user.password)
        if match_password:
            user.set_password(new_password)
            user.save()
            message = f'password successfully changed'
            from django.contrib.auth import authenticate
            u = authenticate(username = user.username, password = new_password)
            login(request, u)
        else:
            message = f'old password is incorrect'
        context['message'] = message
    return render(request, 'user_settings/changePassword.html', context)
    pass
