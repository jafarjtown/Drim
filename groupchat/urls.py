from django.urls import path
from . import views
app_name = 'groupchat'
urlpatterns = [
    path('<str:room_name>/', views.Index, name='group-chat')
]
