from django.http import HttpResponse, FileResponse
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view
from .models import FileUpload 
from .serializers import FileSerializer, RegisterAccount
import mimetypes
import os

class Register(GenericAPIView):
	serializer_class = RegisterAccount
	def post(self,request,*args,**kwargs):
		serializer=self.get_serializer(data=request.data)
		if serializer.is_valid():
			user=serializer.save()
			print(user)
			fkey=User.objects.get(username=user).id
			print(fkey)
		return Response({
				'user': request.data.get('username'),
				'foreign_key': fkey,
				})
	def get(self,request):
		users=[]
		data=User.objects.all()
		data=list(data)
		for i in data:
			users.append((str(i),i.password,i.id))
		return Response(users)

class FileUploader(ViewSet):
	serializer_class = FileSerializer
	def list(self,request):
		return Response("WELCOME TO MGCLOUD BETA API")

	def create(self,request):#post
		file_obj = request.FILES.get('file')
		print(request.data)
		#ct = file_obj.content_type
		file_serializer = FileSerializer(data=request.data)
		print(file_serializer)
		if file_serializer.is_valid(raise_exception=True):
			fname=file_serializer.save()
			fkey = FileUpload.objects.get(file = fname)
			key = fkey.id
			print(key)
			return Response({'status': "File Uploaded To MGCLOUD", 'id':key})
		else:
			return Response('Failed')
	
	def retrieve(self,request,pk):#get
		queryset = FileUpload.objects.get(id=pk)
		path = queryset.file.path
		fhl = queryset.file.open()
		mime_type = mimetypes.guess_type(path)
		response = FileResponse(fhl, content_type='mime_type')
		response['Content-Length'] = fhl.file.size
		response['Content-Disposition'] = "attachment; filename="+queryset.file.name
		print(response)
		return response
	def destroy(self,request,pk):#del
		obj = FileUpload.objects.get(id=pk)
		obj.delete()
		rm = obj.file.path
		os.remove(rm)
		return Response({'status':'Deleted','key':pk})
##		data=FileSerializer(queryset)
##		return Response(data.data)

@api_view(('GET',))
def Userfiles(request,fk):
	data=FileUpload.objects.filter(foreign_key=fk).values()
	print(data)
	return Response({'data':list(data)})
