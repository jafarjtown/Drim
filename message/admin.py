from django.contrib import admin

from .models import UserChatBox, ChatBox, Message, Thread


@admin.register(UserChatBox)
class UserChatBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'user')
    list_filter = ('created_at', 'updated_at', 'user')
    raw_id_fields = ('chats',)
    date_hierarchy = 'created_at'


@admin.register(ChatBox)
class ChatBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at', 'friend')
    list_filter = ('created_at', 'updated_at', 'friend')
    raw_id_fields = ('messages', 'unseen_messages')
    date_hierarchy = 'created_at'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'text', 'file', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id',)
    # list_filter = ('created_at', 'updated_at')
    raw_id_fields = ('chats',)
    # date_hierarchy = 'created_at'