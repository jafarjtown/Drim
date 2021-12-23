from django.db import models
from helpers.models import ModelHelper
# Create your models here.


class Institution(ModelHelper):
    name = models.CharField(max_length=500, unique=True)
    materials = models.ManyToManyField('Files.File', blank=True)
    events = models.ManyToManyField('Event', blank=True)
    programmes = models.ManyToManyField('Programme', blank=True, related_name='institution')
    pages = models.ManyToManyField("pages.Page", blank=True)

    @staticmethod 
    def HigherSubscribe():
        inst = Institution.objects.all()
        higher = 0
        winner = []
        for h in inst.all():
            if h.subscribers.count() > higher:
                higher = h.subscribers.count()
                winner.append({ 'name': h.name , 'number_of_sub' : higher})
            elif h.subscribers.count() == higher:
                prev = winner
                print(prev)
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
