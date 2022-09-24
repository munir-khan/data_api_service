from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from shared_document_store.models import Topic, Folder, Document
from shared_document_store.api.serializers import (TopicSerializer, FolderSerializer, DocumentSerializer)


class TopicView(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class FolderView(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class DocumentView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


