from rest_framework.serializers import Serializer, FileField, ModelSerializer
from django.contrib.auth.models import User
from .models import FileUpload


class RegisterAccount(ModelSerializer):
	class Meta:
		model=User
		fields=['id','username','password']
		
	def Create(self,vali_data):
		user=User.objects.create_user(vali_data['username'],vali_data['password'])
		return user
		
class FileSerializer(ModelSerializer):
	class Meta():
		model = FileUpload
		fields = '__all__'
