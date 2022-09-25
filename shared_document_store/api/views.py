from rest_framework import viewsets

from shared_document_store.models import Topics, Folders, Documents
from shared_document_store.api.serializers import (TopicSerializer, FolderSerializer, DocumentSerializer)


class FolderView(viewsets.ModelViewSet):
    serializer_class = FolderSerializer
    queryset = Documents.objects.all()


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
    queryset = Topics.objects.all()
