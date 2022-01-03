from helpers.models import ModelHelper
from django.db import models
# Create your models here.
import time
from datetime import datetime, timezone
from helpers.utils import _delete_file_
class Post(ModelHelper):
    author = models.ForeignKey(
        'accounts.User', on_delete=models.SET_NULL, null=True,  related_name='posts')
    status = models.TextField()
    likes = models.ManyToManyField('accounts.User')
    files = models.ManyToManyField('Files.File', blank=True)
    comments = models.ManyToManyField('Comment', blank=True)
    related_to = models.CharField(default='normal', max_length=15)

    def get_likes_count(self):
        return int(len(self.likes))

    def delete(self):
        if self.files.count() > 0:
            for file in self.files.all():
                _delete_file_(file.file.path)
        return super().delete()
    
    

    
    class Meta:
        ordering = ['-created_at']

   
class Comment(ModelHelper):
    author = models.ForeignKey(
        'accounts.User', on_delete=models.SET_NULL, null=True)
    status = models.TextField()


class SavedPost(ModelHelper):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='saved_posts')
    posts = models.ManyToManyField('SavePost', blank=True)


class SavePost(ModelHelper):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)


class Story(models.Model):
    upload_on = models.DateTimeField(auto_now_add=True)
    caption = models.TextField()
    file = models.FileField(upload_to=f'stories_files')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='stories', null=True)

    def expire(self):
        t = self.upload_on
        s = datetime.now(timezone.utc)
        if datetime.timestamp(t) + 86400 <= datetime.timestamp(s):
            _delete_file_(self.file.path)
            self.delete() 
            return

        return

