from rest_framework import viewsets
from django.db.models import Q

from shared_document_store.models import Topic, Folder, Document
from shared_document_store.api.serializers import (TopicSerializer, FolderSerializer, DocumentSerializer)


class TopicView(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class FolderView(viewsets.ModelViewSet):
    serializer_class = FolderSerializer

    def get_queryset(self):
        topic = self.request.query_params.get('topic')
        folder = self.request.query_params.get('folder')
        document_ids = Document.objects.filter(topics__name=topic).values_list('id', flat=True)
        folder_document_id = Q(documents_id__in=document_ids)
        folder_name = Q(name=folder)
        query_set = Folder.objects.filter(folder_document_id & folder_name)
        return query_set


class DocumentView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
