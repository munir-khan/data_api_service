from django.contrib import admin

from .models import Folders, Documents, Topics

admin.site.register([Folders, Documents, Topics])
