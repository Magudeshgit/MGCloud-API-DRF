from django.contrib import admin
from django.urls import path, include
from api import views as av
from core import views as cv
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/security',av.Cloudapi,basename='Security')
router.register(r'api/cloud',cv.FileOps,basename='File Operations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))

]
