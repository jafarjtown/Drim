from django.db import models
from helpers.models import ModelHelper
# Create your models here.


class Notification(ModelHelper):
    _from = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='pushed_notification')
    _to = models.ForeignKey(
        'accounts.User', on_delete=models.CASCADE, related_name='received_notification')
    message = models.TextField()