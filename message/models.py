from django.db import models
from helpers.models import ModelHelper
# Create your models here.

class UserChatBox(ModelHelper):
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE, related_name='user_chat')
    chats = models.ManyToManyField("ChatBox", blank=True)

    def unseen(self):
        n = 0
        chats = self.chats.all()
        for chat in chats.all():
            n += chat.unseen_messages.count()
        return n

class ChatBox(ModelHelper):
    friend = models.ForeignKey("accounts.User",on_delete=models.CASCADE)
    messages = models.ManyToManyField("Message")
    unseen_messages = models.ManyToManyField('Message', related_name='unseen_messages')

    def unseen(self):
        seen = self.unseen_messages.all()
        return seen.count()

    def seen(self):
        self.unseen_messages.clear()
    def get_thread_id(self):
        if self.thread:
            return self.thread.all()[0].id

class Message(models.Model):
    sender = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='messages_sent')
    receiver = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='messages_received')
    text = models.TextField()
    file = models.FileField(upload_to='messages/upload/sent/', max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # seen = models.ManyToManyField(Seen)

    def order_by(self):
        return self.created_at


class Thread(models.Model):
    chats = models.ManyToManyField("ChatBox", related_name='thread')