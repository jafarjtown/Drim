from django.urls import path
from . import views
from rest_framework import routers
from .serializers import InstitutionBlogsViewSet, InstitutionViewSet
router = routers.DefaultRouter()

router.register('institutions', InstitutionViewSet)
router.register('institutionsblogs', InstitutionBlogsViewSet)

app_name = 'institution'
urlpatterns = [
    path('', views.Institutions, name='institutions'),
    path('<slug:id>/', views.InstitutionHome, name='institution'),
    path('subscribe/<slug:id>/', views.Subscribe, name='subscribe'),
    path('unsubscribe/<slug:id>/', views.Unsubscribe, name='unsubscribe'),
    path('<slug:id>/programmes', views.Programmes, name='programmes'),
    path('<slug:iid>/programme/<slug:pid>', views.Programme, name='programme'),
    path('<slug:pid>/e-book/<slug:fid>', views.Ebook, name='e-book'),
]
