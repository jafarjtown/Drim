from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, blank=True, max_length=500)
    faculty = models.CharField(max_length=500, blank=True)
    department = models.CharField(max_length=500, blank=True)
    date_of_birth = models.CharField(max_length=10, blank=True)
    followers = models.ManyToManyField(
        'accounts.User', related_name='my_followings', blank=True)
    followings = models.ManyToManyField(
        'accounts.User', related_name='my_followers', blank=True)
    subscribed = models.ManyToManyField(
        'institution.Institution', blank=True, related_name='subscribers')
    activities = models.ManyToManyField("activities.Activity", blank=True)
    avatar = models.ImageField(upload_to = f'upload_avatar()', blank =True)
    pass

    def upload_avatar(self):
        return f'{self.username}_{self.email}'
