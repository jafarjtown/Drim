from django.urls.conf import include
from posts.serializers import PostViewSet, PostViewSetDetail
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


from rest_framework import routers

router = routers.DefaultRouter()

router.register('posts', PostViewSet)
router.register('posts/detail', PostViewSetDetail)


app_name = 'posts'
urlpatterns = [
    path('', include(router.urls)),
    path('<slug:id>/', views.Edit, name='edit'),
    path('save/<slug:id>/', views.savePost, name='save'),
    path('comments/<slug:id>/', csrf_exempt(views.Comment)),
    path('likes/<slug:id>/', csrf_exempt(views.Like)),
]
