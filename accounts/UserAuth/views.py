from django.shortcuts import redirect, render
from accounts.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models.query import Q
from school.models import Faculty
# Create your views here.


def Login(request):
    # print(dir(request.user))
    if request.user.is_authenticated:
        return redirect('home:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get( Q(username=username) | Q(email=username))
            u = authenticate(username=user.username, password=password)
            if u is not None:
                login(request, u)
                return redirect('home:home')
            else:
                message1 = f'wrong password for {username}'
            return render(request, 'auth/index.html', {'message1': message1})
        except:
            message0 = f'sorry, no account with this username or email'
            return render(request, 'auth/index.html', {'message0': message0})
    return render(request, 'auth/index.html')


def Register(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fullName = request.POST['fullname']
        date_of_birth = request.POST['DOB']
        if fullName != '':
            firstname, lastname = fullName.split()
        else:
            firstname = ''
            lastname = ''
        password = request.POST['password1']
        try:
            User.objects.create_user(
                username, email, password, first_name=firstname, last_name=lastname)
                
            return redirect('account:login')
        except IntegrityError as err:
        #     print(err)
            error = f'user with same username or email already exist...'
        except:
            error = f'error occured while submitting the form...'
    faculty = Faculty.objects.all()
    return render(request, 'auth/register.html', {'faculty': faculty, 'error': error})


def PasswordResetRequest(request):
    return render(request, 'auth/forgetPassword.html')

def Logout(request):
    logout(request)
    return redirect('account:login')