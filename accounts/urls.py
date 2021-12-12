from accounts.serializers import UserViewSet
from django.urls import path, reverse
from django.urls.base import reverse_lazy
from . import views
from .UserAuth import views as AuthViews
from django.contrib.auth import views as auth_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserViewSet)
app_name = 'account'
urlpatterns = [
    path('', views.Account, name='account'),
    path('avatar/', views.AddAvatar, name='add-avatar'),
    path('avatar/save', views.saveAvatar, name='save-avatar'),
    path('auth/', AuthViews.Login, name='login'),
    path('auth/register', AuthViews.Register, name='register'),
    path('auth/logout', AuthViews.Logout, name='logout'),
]
