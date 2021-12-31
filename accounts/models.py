from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, blank=True, max_length=500)
    date_of_birth = models.CharField(max_length=10, blank=True)
    followers = models.ManyToManyField(
        'accounts.User', related_name='my_followings', blank=True)
    followings = models.ManyToManyField(
        'accounts.User', related_name='my_followers', blank=True)
    activities = models.ManyToManyField("activities.Activity", blank=True)
    avatar = models.ImageField(upload_to = f'avatars', blank =True)

    def is_teacher(self):
        return Teacher.objects.filter(parent = self).exists()

    def is_student(self):
        return Student.objects.filter(parent = self).exists()
    

    class Meta:
        verbose_name = 'Normal Account'
        verbose_name_plural = 'Normal Account\'s'

class Student(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    course = models.OneToOneField('institution.Course', on_delete=models.SET_NULL, null=True, blank=True)
    pass
    class Meta:
        verbose_name = 'Student Account'
        verbose_name_plural = 'Student Account\'s'

class Teacher(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    students = models.ManyToManyField('Student', blank=True)

    class Meta:
        verbose_name = 'Teacher Account'
        verbose_name_plural = 'Teacher Account\'s'


    