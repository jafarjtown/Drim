from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


app_name = 'cipher'
urlpatterns = [
    path('', views.Index, name='index'),
    path('encript', csrf_exempt(views.encript), name='encript'),
    path('decript', csrf_exempt(views.decript), name='decript'),
]