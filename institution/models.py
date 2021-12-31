from django.db import models
from helpers.models import ModelHelper
# Create your models here.


class Institution(ModelHelper):
    administrator = models.OneToOneField('accounts.User', on_delete=models.SET_NULL, null = True, related_name='administrator')
    tutors = models.ManyToManyField('accounts.Teacher', blank=True)
    name = models.CharField(max_length=500, unique=True)
    slogan = models.CharField(max_length=500)
    logo = models.FileField()
    cover_img = models.FileField()
    website_url = models.URLField()
    address = models.TextField()
    verified = models.BooleanField(default=False)
    blogs = models.ManyToManyField('posts.Post', related_name='institution')
    activities = models.ManyToManyField('activities.Activity')
    materials = models.ManyToManyField('Files.File', blank=True)
    events = models.ManyToManyField('Event', blank=True)
    programmes = models.ManyToManyField('Programme', blank=True, related_name='institution')
    courses = models.ManyToManyField('Course', blank=True)
    pages = models.ManyToManyField("pages.Page", blank=True)
    groups = models.ManyToManyField('groups.Group', related_name='institution')
    subscribers = models.ManyToManyField('accounts.Student', related_name='institutions_subscribes')
    
    @staticmethod 
    def HigherSubscribe():
        inst = Institution.objects.only('subscribers')
        higher = 0
        winner = []
        for h in inst.all():
            if h.subscribers.count() > higher:
                winner = []
                higher = h.subscribers.count()
                winner.append({ 'name': h.name , 'number_of_sub' : higher})
            elif h.subscribers.count() == higher:
                winner.append({'name': h.name, 'number_of_sub' : higher})
        if len(winner) == 1:
            return winner[0]
        else:
            return winner
class Event(ModelHelper):
    name = models.CharField(max_length=100)
    venue = models.CharField(max_length=500)
    from_time = models.DateTimeField(auto_now_add=False, blank=False)
    to_time = models.DateTimeField(auto_now_add=False, blank=False)

class Programme(ModelHelper):
    name = models.CharField(max_length=100)
    materials = models.ManyToManyField('Files.File', blank=True, related_name='programme')
    description = models.TextField()

class Course(ModelHelper):
    title = models.CharField(max_length=100)
    slogan = models.CharField(max_length=200)
