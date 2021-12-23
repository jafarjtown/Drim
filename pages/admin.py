from django.contrib import admin

from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'name',
        'website_url',
        'about',
        'verification_code',
    )
    list_filter = ('created_at', 'updated_at')
    raw_id_fields = ('followers', 'posts', 'admins')
    search_fields = ('name',)
    date_hierarchy = 'created_at'
