from django.contrib import admin

from .models import Group, Rule, ForbiddenWord, Event


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
       
        'creator',
        'name',
        'description',
    )
    list_filter = ('created_at','creator')      
    raw_id_fields = ('admins', 'members', 'rules', 'events')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at',  'rule', 'strick')
    list_filter = ('created_at','strick')       
    raw_id_fields = ('forbiden_words',)
    date_hierarchy = 'created_at'


@admin.register(ForbiddenWord)
class ForbiddenWordAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at',  'word')  
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at',  'name')  
    list_filter = ('created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'