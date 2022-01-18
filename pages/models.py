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
    img = models.ImageField()
    cover = models.ImageField()
    
    def get_img(self):
        if self.img != '':
            return self.img.url
        return '/static/media/images/david-r-cook.jpg'
    
    def get_cover(self):
        if self.cover != '':
            return self.cover.url
        return '/static/media/images/cristy-gowen.jpg'
    

    def get_all_posts(self):
        return self.posts.all()