from rest_framework import serializers
from api.models import Users
from .models import FileLog

class SharedWithUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id']

class FileSerializer(serializers.ModelSerializer):
    sharedwith = SharedWithUserSerializer(many=True)
    owner = SharedWithUserSerializer()
    class Meta:
        model = FileLog
        fields = '__all__'