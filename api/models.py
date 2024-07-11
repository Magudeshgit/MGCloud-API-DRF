from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class Users(models.Model):
    mail = models.EmailField()
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    session_id = models.CharField(max_length=50,)
    expiration = models.DateTimeField()
    
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

