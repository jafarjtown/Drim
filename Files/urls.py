from rest_framework import routers

from Files.views import  addFile, createFolderMain, createSubFolder, deleteFolderItem, mainFolder, subFolder
from .serializers import FileViewSet
from django.urls import path
router = routers.DefaultRouter()

router.register('files', FileViewSet)

app_name = 'files'
urlpatterns = [
    path("main.folder/", mainFolder, name="main"),
    path("main.folder/<slug:folder_id>.user.<slug:user_id>/", subFolder, name="sub"),
    path("main.folder/view.<slug:folder_id>.user.<slug:user_id>/", subFolder, name="view_folder"),
    path("main.folder.create/", createFolderMain, name="create_main"),
    path("main.subfolder.create/<slug:id>/", createSubFolder, name="create_folder"),
    path("main.subfolder.add.file/<slug:id>/", addFile, name="add_file"),
    path("main.subfolder.delete.file/<slug:id>/", deleteFolderItem, name="delete_file"),
]
