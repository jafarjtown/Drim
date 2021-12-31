"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('', include('home.urls')),
    # path('notes/', include('notes.urls')),
    path('faculty/', include('school.urls')),
    path('posts/', include('posts.urls')),
    path('pages/', include('pages.urls')),
    path('groups/', include('groups.urls')),
    path('groupchat/', include('groupchat.urls')),
    path('settings/', include('settings.urls')),
    path('friends/', include('friends.urls')),
    path('activities/', include('activities.urls')),
    path('notifications/', include('notifications.urls')),
    path('institution/', include('institution.urls')),
    path('messenger/', include('message.urls')),
    path('market/', include('market.urls')),
    path('api/', include('mainApi.urls')),
    path('api/auth/', include('rest_auth.urls')),
    path('api/auth/register', include('rest_auth.registration.urls')),
    path('search/', include('search.urls')),
    path('reset_password/', auth_view.PasswordResetView.as_view(
         template_name='auth/forgetPassword.html',
         ), name='password_reset'),
    path('reset_password/done', auth_view.PasswordResetDoneView.as_view(
        template_name='auth/forgetPasswordDone.html'
    ),
        name='password_reset_done'),

    path('reset_password/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(
             template_name='auth/forgetPasswordCom.html'

         ), name='password_reset_confirm'),

    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(
        template_name='auth/forgetPasswordComplete.html'

    ),
        name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = 'home.views.Home'

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
