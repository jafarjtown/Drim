
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

def _upload_user_path(instance, filename):
    return instance.get_upload_path(filename)

class User(AbstractUser):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, blank=True, max_length=500)
    date_of_birth = models.CharField(max_length=10, blank=True)
    followers = models.ManyToManyField(
        'accounts.User', related_name='my_followings', blank=True)
    followings = models.ManyToManyField(
        'accounts.User', related_name='my_followers', blank=True)
    activities = models.ManyToManyField("activities.Activity", blank=True)
    avatar = models.ImageField(upload_to = _upload_user_path, blank =True)
    cover = models.ImageField(upload_to = _upload_user_path, blank =True)
    contacts = models.ManyToManyField('Contact', blank=True)
    
    def get_upload_path(self, filename):
        return 'imgs/' +  str(self.username)+ '/avatar_cover/' + filename
    def is_teacher(self):
        return Teacher.objects.filter(parent = self).exists()

    def is_student(self):
        return Student.objects.filter(parent = self).exists()
    def get_avatar(self):
        if self.avatar != '':
            return self.avatar.url
        return 'http://127.0.0.1:8000/static/media/images/default_image.jpg'
    def get_cover(self):
        if self.cover != '':
            return self.cover.url
        return 'http://127.0.0.1:8000/static/img/cover/cv.jpg'
    def get_students(self):
        return self.teacher.students.all()
    def get_tutors(self):
        return self.student.tutors.all()
    def has_page(self):
        if self.pages.count() > 0:
            return True
        return False
    def friends_pages(self):
        pages = []
        for friend in self.followings.all():
            if friend.has_page():
                for page in friend.pages.all():
                    pages.append(page)
        return pages
    class Meta:
        verbose_name = 'Normal Account'
        verbose_name_plural = 'Normal Account\'s'

class Student(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student')
    course = models.OneToOneField('institution.Course', on_delete=models.SET_NULL, null=True, blank=True)
    tutors = models.ManyToManyField('Teacher', blank=True)
    
    def get_full_name(self):
        parent = self.parent
        if parent.first_name != '':
            return parent.get_full_name()
        return parent.username
    
    def get_avatar(self):
        parent = self.parent
        if parent.avatar != '':
            return parent.avatar.url
        return 'http://127.0.0.1:8000/static/img/logo/logo.png'
    pass
    class Meta:
        verbose_name = 'Student Account'
        verbose_name_plural = 'Student Account\'s'

class Teacher(models.Model):
    parent = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher')
    students = models.ManyToManyField('Student', blank=True)

    def get_full_name(self):
        parent = self.parent
        if parent.first_name != '':
            return parent.get_full_name()
        return parent.username
    
    def get_avatar(self):
        parent = self.parent
        if parent.avatar != '':
            return parent.avatar.url
        return 'http://127.0.0.1:8000/static/img/logo/logo.png'
    class Meta:
        verbose_name = 'Teacher Account'
        verbose_name_plural = 'Teacher Account\'s'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    resipient =models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    
    def get_name(self):
        if self.name == '':
            return self.resipient.username
        return self.name
    
    