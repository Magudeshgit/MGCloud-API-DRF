from django.contrib import admin
from django.urls import path, include
from api import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cloud',views.FileUploader,basename='cloud')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('accounts/',views.Register.as_view()),
    path('userfiles/<str:fk>',views.Userfiles),
#    path('auth/',views.Authenticate)

]
