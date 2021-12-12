from django.db import models
from helpers.models import ModelHelper
# Create your models here.

class Activity(ModelHelper):
    activity = models.CharField(max_length=50)
    description = models.TextField()
    