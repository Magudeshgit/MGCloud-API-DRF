from django.contrib import admin
from .models import FileLog

admin.site.name = "MGCloud API"
admin.site.site_title = "MGCloud API V2"
admin.site.register([FileLog])