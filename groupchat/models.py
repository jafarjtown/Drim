from django.db import models

# Create your models here.


class OneToOneGroup(models.Model):
    users = models.ManyToManyField('accounts.User',related_name='threed')
    