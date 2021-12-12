from rest_framework import routers
from .serializers import FileViewSet
router = routers.DefaultRouter()

router.register('files', FileViewSet)
