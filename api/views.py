from django.http import HttpResponse, FileResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Users
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import UserSerializer
from django.utils import timezone
import requests as r
from .authhelper import authenticate as InternalAuthenticate, Credentialauth

# API Endpoints
# mgauth = 'https://mgauthsphere.pythonanywhere.com/api/'
#mgauth = 'http://127.0.0.1:7000/api/'
mgauth = 'http://127.0.0.1:7000/api/'
TOKEN = 'a3e2935779c2f87c61ab3f54fc953944e94ebf27'#'5fcec46340e08e0a9d1c0a36594bef36bbe300e4'#'4ef2662150db3265354c604958e3df87f4defe90'
APP_PASSWORD = 'iZW1ddCywQCMXp5dEMEy8BkCRKURcUsJ'

class Cloudapi(ModelViewSet):
    queryset = Users.objects.all()
    
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    

    @action(detail=False, methods=['post'])
    def checksession(self, request):
        try:
            sessionid = request.data['session_id']
        except KeyError:
            return Response({
                "status": "failed",
                "detail": "insufficient parameters"
                }, status=status.HTTP_400_BAD_REQUEST)
        
      
        auth = InternalAuthenticate(session_id=sessionid)
        if auth:
            a=UserSerializer(auth)
            return Response({
                "status":"success", 
                "detail": "user Authenticated",
                "user": a.data,
            },
                            status=status.HTTP_200_OK)
        else:
            return Response({
                "status":"failed", 
                "detail": "authentication failed"
            },
                            status=status.HTTP_403_FORBIDDEN)
            
    @action(detail=False, methods=['post'])
    def createuser(self, request):
        try:
            _email = request.data['email']
            _password = request.data['password']
        except KeyError:
            return Response({
                "status": "failed",
                "detail": "insufficient parameters, required email and password"
                }, status=status.HTTP_400_BAD_REQUEST)
            
        _optional_fields = ['first_name','last_name']
        optional_fields = {'first_name': '', 'last_name': ''}
        for field in _optional_fields:
            if request.data.get(field) != None:
                optional_fields[field] = request.data.get(field)
        print("XXX", optional_fields)
            
        # API OPS
        _data={
                'email': _email,
                'password': _password,
                'first_name': optional_fields['first_name'],
                'last_name': optional_fields['last_name'],
                'app_key': APP_PASSWORD
            }
        print(_data)
        resp = r.post(
            mgauth + 'createuser/',
            headers={
                'Authorization': 'Token ' + TOKEN 
            },
            data=_data
        )
        print(resp)
        data = resp.json()
        print(data)
        if data['status'] == 'success':
            self.queryset.create(mail=data['email'], 
                                 session_id=data['session_id'], 
                                 expiration=data['session_expiry'],
                                 firstname=data['first_name'],
                                 lastname=data['last_name'],
                                 )
            return Response({"status": "success", "data": data})
        else:
            return Response({"status": "failed", "data": 'Operation failed'})
        
    @action(detail=False, methods=['post'])
    def authenticate(self, request):
        try:
            _email = request.data['email']
            _password = request.data['password']
        except KeyError:
            return Response({
                "status": "failed",
                "detail": "insufficient parameters, required email and password"
                }, status=status.HTTP_400_BAD_REQUEST)
        payload = {
            'email': _email,
            'password': _password
        }
        
        response = r.post(mgauth + 'authenticate/',
               headers={
                'Authorization': 'Token ' + TOKEN 
                },
                data=payload)
        
        response = response.json()
        if response['status'] == 'success':
            user, created = self.queryset.get_or_create(mail=_email)
            user.session_id = response['session_id']
            user.expiration = response['session_expiry']
            user.save()
            return Response(response)
        else:
            return Response({'status': 'failed', 'detail': 'Authentication failed, there is no such user'})
    
    # @action(detail=False, methods=['post'])
    # def getsymkey(self, request):
    #     response = r.post(mgauth + 'getsymmetrickey/',
    #            headers={
    #             'Authorization': 'Token ' + TOKEN 
    #             },
    #             data={
    #                 "app_key": APP_PASSWORD
    #             })
    #     return Response(response.json())
    
    def get_view_name(self):
        return "MGCloud V2"