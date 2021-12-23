from django.urls import path
from . import views

app_name = 'school'

from rest_framework import routers
from .serializers import FacultyViewSet
router = routers.DefaultRouter()

router.register('faculties', FacultyViewSet)

urlpatterns = [
    path('<str:faculty>', views.getLocalGov, name='get_local_gov'),
    path('', views.Institutions, name='institutions'),
]
