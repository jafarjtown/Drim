from django.db import models
from helpers.models import ModelHelper
import os
# Create your models here.

class File(ModelHelper):
    name = models.CharField(max_length=100)
    file = models.FileField()
    
    def get_name(self):
        return os.path.basename(self.file.name)

def SubFoldersSizes(folders, s = 0):
    ss = s
    for f in folders:
        ss += 100
        for fi in f.items.all():
            ss +=  fi.file.size
        if len(f.subfolders.all()) > 0:
            ss += SubFoldersSizes(f.subfolders.all())
    return ss
  
class MainFolder(ModelHelper):
    name = models.CharField(max_length=100)
    subfolders = models.ManyToManyField('Folder', blank=True)
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='main_folder')
    items = models.ManyToManyField(File, blank=True)
    private = models.BooleanField(default=True)
    
    def get_public(self):
        return self.objects.filter(private = False)
    
    def size(self):
        s = 0
        # each folder == 100kb
        s += SubFoldersSizes(self.subfolders.all())
        for f in self.items.all():
            s += f.file.size
        s =  s / 1024
        if s > 1000:
            return f'{round(s / 1024)}mb' 
        return f'{round(s)}kb'
        # how to get files from subfolders??

class Folder(ModelHelper):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(File, blank=True)
    subfolders = models.ManyToManyField('Folder', blank=True)
    private = models.BooleanField(default=True)
    
    def get_public(self):
        return self.objects.filter(private = False)
    
    def size(self):
        s = 0
        # each folder == 100kb
        s += SubFoldersSizes(self.subfolders.all())
        for f in self.items.all():
            s += f.file.size
        s =  s / 1024
        if s > 1000:
            return f'{round(s / 1024)}mb' 
        return f'{round(s)}kb'
        # how to get files from subfolders??
