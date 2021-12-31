from django.contrib import admin

from .models import Post, Comment, Story


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at')
    list_filter = ('created_at',)
    raw_id_fields = ('likes', 'comments')
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author',)
    list_filter = ('author',)

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload_on',)
    list_filter = ('upload_on',)
