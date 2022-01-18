from accounts.serializers import UserViewSet
from django.urls import path, reverse
from django.urls.base import reverse_lazy
from . import views
from .UserAuth import views as AuthViews
from django.contrib.auth import views as auth_view
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register('users', UserViewSet)
app_name = 'account'
urlpatterns = [
    path('', views.Account, name='account'),
    path('type/student', views.studentAccount, name='student_create'),
    path('type/tutor', views.tutorAccount, name='tutor_create'),
    path('<slug:id>/profile', views.ViewAccount, name='profile'),
    path('avatar/', views.AddAvatar, name='add-avatar'),
    path('avatar/save', views.saveAvatar, name='save-avatar'),
    path('contact/create', views.createContact, name='create_contact'),
    
    
    path('auth/', AuthViews.Login, name='login'),
    path('auth/register', csrf_exempt(views.registerUser), name='register'),
    path('auth/logout', AuthViews.Logout, name='logout'),
    path('auth/verify', csrf_exempt(views.VerifyEmail), name='verify_email'),
    path('auth/login/', csrf_exempt(views.loginUser), name='login_user'),
]
