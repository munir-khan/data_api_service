from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TopicView, DocumentView, FolderView


router = DefaultRouter()
router.register(r'topic', TopicView, basename="topic")
router.register(r'folder', FolderView, basename="folder")
router.register(r'document', DocumentView, basename="document")


urlpatterns = [
    path('', include(router.urls)),
]
