from django.urls import path
from . import views
app_name = 'notifications'
from rest_framework import routers
from .serializers import NotificationViewSet
router = routers.DefaultRouter()

router.register('notifications', NotificationViewSet)

urlpatterns = [
    path('', views.Index, name='notification_page')
]
