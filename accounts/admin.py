
from django.contrib import admin

from .models import Contact, User, Student, Teacher


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'id'
        
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )
    raw_id_fields = (
        'groups',
        'user_permissions',
        'followers',
        'followings',
        'activities',
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'course')
    list_filter = ('parent', 'course')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent')
    list_filter = ('parent',)
    raw_id_fields = ('students',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'resipient')
    list_filter = ('resipient',)