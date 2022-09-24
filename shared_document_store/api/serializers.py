from rest_framework import serializers
from shared_document_store.models import Topic, Folder, Document


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(many=True, read_only=True)
    folder = FolderSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ['name', 'type', 'path', 'topic', 'folder']
