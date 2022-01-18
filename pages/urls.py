from rest_framework import routers
from .serializers import PageViewSet
from . import views
from django.urls import path
router = routers.DefaultRouter()

router.register('pages', PageViewSet)

app_name='pages'

urlpatterns = [
    path('', views.Index, name='index'),
    path('code/', views.HomePages, name='home-pages'),
    path('name/', views.HomePagesName, name='home-pages-name'),
    path('<str:name>/<slug:id>/', views.HomePage, name='home-page'),
    path('<str:name>/<slug:id>/admins', views.VerficationPage, name='verification-page'),
    path('create/', views.CreatePage, name='create-page'),
    path('follow/<slug:pgi>/page/', views.FollowUnfollowPage, name='follow-page'),
]
