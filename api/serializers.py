from rest_framework.serializers import Serializer, FileField, ModelSerializer
from django.contrib.auth.models import User
from .models import  Users
  
class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
