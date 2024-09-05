from django.contrib import admin
from django.contrib.auth.models import User, Group
from rest_framework.authtoken.models import Token
from .models import Users
# Register your models here.

admin.site.unregister([Group, User])
admin.site.register([Users])