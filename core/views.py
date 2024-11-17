from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action


from api.models import Users
from .models import FileLog, DirectoryLog
from .serializer import FileSerializer, DirectorySerializer

from .helper import *
from .sourceview import FileAbstract

class FileOps(FileAbstract):
    @action(detail=False, methods=['post'])
    def userfiles(self, request):
        user = Users.objects.get(user_id = request.data.get('userid'))
        response = self.queryset.filter(owner=user).order_by('-date_created')
        response = FileSerializer(response, many=True).data
        return Response(response)
        
    @action(detail=False, methods=['post'])
    def userdirectories(self, request):
        user = Users.objects.get(user_id = request.data.get('userid'))
        directories = DirectoryLog.objects.filter(owner=user)
        
        response = DirectorySerializer(directories, many=True).data
        return Response(response)
    
    @action(detail=False, methods=['post'])
    def generatepresignedurl(self, request):
        files = request.data.get('files')
        if not files:
            return Response({"status":"failed", "detail": "insufficient parameters, please provide file names"})
        urlpack = {}
        for filename in files:
            urlpack[filename] = UploadPresignedUrl(filename)
        return Response(urlpack)
    
    @action(detail=False, methods=['post'])
    def adduserfiles(self, request):
        userfiles = request.data.get('files')
        user = Users.objects.get(user_id = request.data.get('userid'))
        data_array=[]
        for file in userfiles:
            fileinst = FileLog(filename=file['filename'], 
                                filesize=file['filesize'], 
                                filetype="example", 
                                relativepath="",
                                owner=user
                                )
            data_array.append(fileinst)
        self.queryset.bulk_create(data_array)
        
        return Response({"status":"success", "detail": "Data saved"})
    
    @action(detail=False, methods=['post'])
    def getfileurl(self, request):
        filename = request.data.get("filename")
        presignedurl = getFileURLForPreview(filename)
        return Response({"status": "success", "url":presignedurl})
    
    @action(detail=False, methods=['post'])
    def getfiledownloadurl(self, request):
        filename = request.data.get("filename")
        presignedurl = getFileURLForDownload(filename)
        return Response({"status": "success", "url":presignedurl})
    
    @action(detail=False, methods=['post'])
    def modifyfilefavourite(self, request):
        
        fileid = request.data.get("fileid")
        operationtype = request.data.get("addfavourite")
        user = Users.objects.get(user_id = request.data.get('userid'))
        print("FILEFAV", operationtype)
        fileobj = FileLog.objects.get(id=fileid)
        
        
        if fileobj.owner != user:
            return Response({"success": False, "detail":"PermissionError: This User doesnt have permission to modify a file owned by other"})
        if operationtype:
            fileobj.isFavourite = True
        else:
            fileobj.isFavourite = False
        fileobj.save()
        return Response({"success": True, 
                         "details":[
                             {
                                "message":"File modified",
                                "isFavourite": operationtype
                             }
                             ]})