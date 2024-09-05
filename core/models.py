from django.db import models
from api.models import Users


class FileLog(models.Model):
    filename = models.CharField(max_length=100)
    filesize = models.CharField(max_length=20)
    filetype = models.CharField(max_length=20)
    relativepath = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    
    isMgsecure = models.BooleanField(default=False)
    isShared = models.BooleanField(default=False)
    isFavourite = models.BooleanField(default=False)
    
    sharedwith = models.ManyToManyField(Users, blank=True, related_name='sharedwith')
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.filename