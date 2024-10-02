from django.db import models
from api.models import Users


class FileLog(models.Model):
    filename = models.CharField(max_length=100)
    filesize = models.CharField(max_length=20)
    filetype = models.CharField(max_length=20)
    relativepath = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    isMgsecure = models.BooleanField(default=False)
    isShared = models.BooleanField(default=False)
    isFavourite = models.BooleanField(default=False)
    inDirectory = models.ForeignKey('DirectoryLog', on_delete=models.CASCADE, null=True, blank=True)
    
    sharedwith = models.ManyToManyField(Users, blank=True, related_name='sharedwith')
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.filename
    
class DirectoryLog(models.Model):
    parentDir = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    dirName = models.CharField(max_length=50)
    fileCount = models.PositiveIntegerField(null=True)
    diskSize = models.CharField(max_length=50)
    createdOn = models.DateField()
    owner = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    isSecure = models.BooleanField(default=False)
    isSubdir = models.BooleanField(default=False)
    passCode = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self):
        return self.dirName