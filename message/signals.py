from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from accounts.models import User
from .models import UserChatBox


@receiver(post_save, sender=User)
def create_user_chat_box(sender, instance, created, **kwargs):
    if created:
        UserChatBox.objects.create(user = instance)
    pass