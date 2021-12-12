from django.db import models
from helpers.models import ModelHelper
# Create your models here.

class File(ModelHelper):
    name = models.CharField(max_length=100)
    file = models.FileField(unique=True)

   