from django.contrib import admin

from .models import Institution, Event, Programme


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    raw_id_fields = ('materials', 'events', 'programmes')
    search_fields = ('name',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'venue',
        'from_time',
        'to_time',
        'created_at',
    )
    list_filter = ('from_time', 'to_time', 'created_at')
    search_fields = ('name',)
    date_hierarchy = 'created_at'


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    raw_id_fields = ('materials',)
    search_fields = ('name',)
