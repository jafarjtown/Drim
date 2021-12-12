from django.contrib import admin

from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'activity',
        'description',
    )
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'