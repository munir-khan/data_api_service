from rest_framework import viewsets

from shared_document_store.models import Topics, Folders, Documents
from shared_document_store.api.serializers import (TopicSerializer, FolderSerializer, DocumentSerializer)


class FolderView(viewsets.ModelViewSet):
    serializer_class = FolderSerializer

    def get_queryset(self):
        folder_name = self.request.query_params.get('name')
        query_set = Folders.objects.all()
        if folder_name:
            query_set = Folders.objects.filter(name=folder_name)
        return query_set


class DocumentView(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        topic = self.request.query_params.get('topic')
        folder = self.request.query_params.get('folder')
        if topic and folder:
            query_set = Documents.objects.filter(topic__name=topic.title()).filter(folder__name=folder.title()).all()
        else:
            query_set = Folders.objects.all()
        return query_set


class TopicView(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    # lookup_field = 'name'

    def get_queryset(self):
        topic_name = self.request.query_params.get('name')
        query_set = Topics.objects.all()
        if topic_name:
            query_set = Topics.objects.filter(name=topic_name)
        return query_set
