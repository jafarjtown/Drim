from django.db import models
from helpers.models import ModelHelper
# Create your models here.


class Page(ModelHelper):
    name = models.CharField(max_length=50)
    website_url = models.URLField(blank=True)
    about = models.TextField(default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Adipisci sed inventore facilis rem delectus debitis. Corrupti delectus, ex, similique recusandae fugit aliquam vitae aliquid magnam ullam illo quaerat incidunt quia.')
    followers = models.ManyToManyField('accounts.User', related_name='pages_followed', blank=True)
    posts = models.ManyToManyField("posts.Post", blank=True, related_name='page')
    admins = models.ManyToManyField('accounts.User', related_name='pages')
    verification_code = models.CharField(max_length=15)
    verify = models.BooleanField(default=False)
    

    def get_all_posts(self):
        return self.posts.all()

# class PagePost(ModelHelper):
#     author = models.ForeignKey(
#         'accounts.User', on_delete=models.SET_NULL, null=True,  related_name='page_posts')
#     status = models.TextField()
#     likes = models.ManyToManyField('accounts.User', related_name='page_post_likes')
#     dislikes = models.ManyToManyField('accounts.User', related_name='page_post_dislikes')
#     files = models.ManyToManyField('Files.File', blank=True)
#     comments = models.ManyToManyField('PageComment', blank=True)
#     page = models.ForeignKey('pages.Page', null=True, related_name='all_posts', on_delete=models.CASCADE)

#     class Meta:
#         ordering = ['-created_at']

   
# class PageComment(ModelHelper):
#     author = models.ForeignKey(
#         'accounts.User', on_delete=models.SET_NULL, null=True)
#     status = models.TextField()
