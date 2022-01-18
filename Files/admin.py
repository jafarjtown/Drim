from django.contrib import admin

from .models import File, Folder, MainFolder


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'file')
    search_fields = ('name',)

@admin.register(MainFolder)
class MainFolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
