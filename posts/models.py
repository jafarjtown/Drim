from helpers.models import ModelHelper
from django.db import models
# Create your models here.


class Post(ModelHelper):
    author = models.ForeignKey(
        'accounts.User', on_delete=models.SET_NULL, null=True,  related_name='posts')
    status = models.TextField()
    likes = models.ManyToManyField('accounts.User')
    files = models.ManyToManyField('Files.File', blank=True)
    comments = models.ManyToManyField('Comment', blank=True)
    group = models.ForeignKey('groups.Group', null=True, related_name='group_post', on_delete=models.CASCADE)

    def get_likes_count(self):
        return int(len(self.likes))
    
    class Meta:
        ordering = ['-created_at']

   
class Comment(ModelHelper):
    author = models.ForeignKey(
        'accounts.User', on_delete=models.SET_NULL, null=True)
    status = models.TextField()
