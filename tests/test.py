import json
from os.path import join
from http import HTTPStatus

from django.conf import settings
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from rest_framework.test import force_authenticate
from rest_framework.test import APIClient

# from api.views import DogViewSet
# from api.models import Dog

from shared_document_store.api.views import TopicView, FolderView, DocumentView
from shared_document_store.models import Topics, Folders, Documents


class TopicViewSetTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username='munir',
            password='test123',
            email='munir@test.com'
        )
        # Create a topic
        self.topic = Topics.objects.create(
            name="Topic_1",
            description='Topic_1 desc'
        )
        # Create a folder
        self.folder = Folders.objects.create(
            name='folder2',
            path="folder1/folder2"
        )

    def test_topic_viewset(self):
        """ Fetch a topic from the test db"""

        request = self.factory.get('/topic?name=Topic_1')
        view = TopicView.as_view({'get': 'list'})
        response = view(request)
        # Check if the name is Topic_1, like it is in the newly created topic:
        self.assertEqual(response.data[0]['name'], 'Topic_1')
        # Check if you get a 200 back:
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_folder_viewset(self):
        """ Fetch a folder from the test db"""

        request = self.factory.get('/folder?name=folder2')
        view = FolderView.as_view({'get': 'list'})
        response = view(request)
        # Check if the name is folder2, like it is in the newly created topic:
        self.assertEqual(response.data[0]['name'], 'folder2')
        # Check if you get a 200 back:
        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_topic_create(self):
        """ Create a topic in the test db"""

        data = json.dumps({
            "name": "Topic_2",
            "description": "Topic_2 desc"
        })
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/topic/', data=data, content_type='application/json')
        # Check if you get a 200 back:
        self.assertEqual(response.status_code, HTTPStatus.CREATED._value_)
        # Check to see if Wishbone was created
        self.assertEqual(response.data['name'], 'Topic_2')

    def test_folder_create(self):
        """ Create a folder in the test db"""
        data = json.dumps({
            "name": "folder3",
            "path": "folder2/folder3/"
        })
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/folder/', data=data, content_type='application/json')
        # Check if you get a 200 back:
        self.assertEqual(response.status_code, HTTPStatus.CREATED._value_)
        # Check to see if folder3 was created
        self.assertEqual(response.data['name'], 'folder3')

    def test_document_create(self):
        """ Get the folder and topic id and then create the document"""

        request = self.factory.get('/topic?name=Topic_1')
        view = TopicView.as_view({'get': 'list'})
        response = view(request)
        topic_id = response.data[0]['id']

        request = self.factory.get('/folder?name=folder2')
        view = FolderView.as_view({'get': 'list'})
        response = view(request)
        folder_id = response.data[0]['id']

        data = json.dumps({
            "name": "document1.png",
            "folder_path": folder_id,
            "topic_name": topic_id
        })
        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post('/document/', data=data, content_type='application/json')
        # Check if you get a 200 back:
        self.assertEqual(response.status_code, HTTPStatus.CREATED._value_)
        # Check to see if document1.png was created
        self.assertEqual(response.data['name'], 'document1.png')
