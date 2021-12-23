from django.db import models
from helpers.models import ModelHelper
# Create your models here.


class Group(ModelHelper):
    creator = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)
    admins = models.ManyToManyField('accounts.User', related_name='operating_groups', blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    members = models.ManyToManyField('accounts.User', related_name='groups_in',blank=True)
    rules = models.ManyToManyField('Rule',blank=True)
    events = models.ManyToManyField('Event',blank=True)
    # posts = models.ManyToManyField('posts.Post', blank=True)
    w_posts = models.ManyToManyField('posts.Post', blank=True, related_name='post_against_rule')
    private = models.BooleanField(default=False)

class Rule(ModelHelper):
    rule = models.CharField(max_length=500)
    strick = models.BooleanField(default=False)
    forbiden_words = models.ManyToManyField('ForbiddenWord', blank=True)

class ForbiddenWord(ModelHelper):
    word = models.CharField(max_length=20)

class Event(ModelHelper):
    name = models.CharField(max_length=400)
