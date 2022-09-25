from rest_framework import serializers

from shared_document_store.models import Topics, Folders, Documents


class FolderSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Folders
        fields = "__all__"

    def create(self, validated_data):
        path = validated_data['path']
        path_exist = Folders.objects.filter(path=path).first()
        if not path_exist:
            folder_name = list(filter(None, path.split('/')))[-1]
            validated_data['name'] = folder_name
        else:
            raise serializers.ValidationError({"error": "path already exist"})
        return super(FolderSerializer, self).create(validated_data)


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = "__all__"

    def create(self, validated_data):
        validated_data.update({'name': validated_data['name'].title()})
        return super(TopicSerializer, self).create(validated_data)


class DocumentSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    folder = FolderSerializer(read_only=True)
    topic_name = serializers.PrimaryKeyRelatedField(
        queryset=Topics.objects.all(), source='topic', write_only=True)
    folder_path = serializers.PrimaryKeyRelatedField(
        queryset=Folders.objects.all(), source='folder', write_only=True)

    class Meta:
        model = Documents
        fields = "__all__"
