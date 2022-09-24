
from rest_framework import serializers


from shared_document_store.models import Topic, Folder, Document


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    document = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Folder
        exclude = ('name',)

    def create(self, validated_data):
        path = validated_data['path']
        path_exist = Folder.objects.filter(path=path).first()
        if not path_exist:
            folder_name = path.split('/')[-1]
            validated_data['name'] = folder_name
        else:
            raise serializers.ValidationError({"error": "path already exist"})
        return super(FolderSerializer, self).create(validated_data)