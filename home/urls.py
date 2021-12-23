from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.Home, name='home'),
    # path('create/', csrf_exempt(views.createNewPost), name='create_new_post')
]
