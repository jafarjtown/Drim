from django.urls import path
from .views import UserActivities, UserChangePAssword, UserInstitution, UserPersonalInfo, UserSetting
from django.contrib.auth import views as auth_view
app_name = 'settings'

urlpatterns = [
    path('me/', UserSetting, name='user_settings'),
    path('me/personal', UserPersonalInfo, name='user_personal'),
    path('me/personal/change_password', UserChangePAssword, name='user_change_password'),
    path('me/activities', UserActivities, name='user_activities'),
    path('me/institution', UserInstitution, name='user_institution'),


   
]
