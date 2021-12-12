from django.urls import path
from . import views
from .serializers import ActivityViewSet
app_name='activity'
from rest_framework import routers

router = routers.DefaultRouter()

router.register('activities', ActivityViewSet)

urlpatterns = [
    path('me/', views.Index, name='activities'),
    path('me/clear_all', views.ClearAll, name='activities_clear')
]

