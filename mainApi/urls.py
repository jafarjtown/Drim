import notifications
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter, SimpleRouter
from posts.urls import router as post_router
from institution.urls import router as institution_router
from activities.urls import router as activities_router
from groups.urls import router as groups_router
from Files.urls import router as files_router
from message.urls import router as message_router
from pages.urls import router as pages_router
from school.urls import router as school_router
from notifications.urls import router as notification_router
from accounts.urls import router as accounts_router
router = DefaultRouter()
router.root_view_name = 'Jafar API'

urlpatterns = [
    path('', include(router.urls)),
    path('post/', include(post_router.urls)),
    path('user/', include(accounts_router.urls)),
    path('file/', include(institution_router.urls)),
    path('activity/', include(activities_router.urls)),
    path('school/', include(school_router.urls)),
    path('page/', include(pages_router.urls)),
    path('group/', include(groups_router.urls)),
    path('message/', include(message_router.urls)),
    path('notification/', include(notification_router.urls)),
    path('institution/', include(institution_router.urls))

]
