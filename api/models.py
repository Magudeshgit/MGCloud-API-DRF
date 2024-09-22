from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class Users(models.Model):
    mail = models.EmailField()
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    user_id = models.CharField(max_length=50, null=True)
    
    session_id = models.CharField(max_length=50,)
    expiration = models.DateTimeField()
    
    # Integrations
    google_access = models.TextField(null=True, blank=True)
    dropbox_access = models.TextField(null=True, blank=True)
    onedrive_access = models.TextField(null=True, blank=True)
    
    
    def __str__(self):
        return self.mail
    class Meta:
        verbose_name = "MGCloud User"
        verbose_name_plural = "MGCloud Users"

# "id": 1,
# "username": "Magudesh",
# "email": "magudesh2006@gmail.com",
# "signed_services": [],
# "session_id": "yn9wuqlrltbxiyvaeg2qwxant5hg25sg"
