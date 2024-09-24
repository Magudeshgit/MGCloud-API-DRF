from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


from api.models import Users
from .models import FileLog, DirectoryLog
from .serializer import FileSerializer, DirectorySerializer

from .helper import *


class FileAbstract(ModelViewSet):
    queryset = FileLog.objects.all()
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = FileSerializer
    dir_serializer_class = DeprecationWarning
    
            
    def get_view_name(self):
        return "MGCloud V2"