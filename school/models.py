from helpers.models import ModelHelper
from django.db import models
# Create your models here.


class Faculty(ModelHelper):
    name = models.CharField(unique=True, max_length=150)
    departments = models.ManyToManyField('Department', blank=True)


class Department(ModelHelper):
    name = models.CharField(max_length=150)
