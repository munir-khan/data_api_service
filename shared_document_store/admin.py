from django.contrib import admin

from .models import Folder, Document, Topic

admin.site.register([Folder, Document, Topic])
