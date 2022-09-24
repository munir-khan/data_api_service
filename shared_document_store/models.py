from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Topic(Base):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Document(Base):
    name = models.CharField(max_length=50)
    topics = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Folder(Base):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=700, default=None)
    documents = models.ForeignKey(Document, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
