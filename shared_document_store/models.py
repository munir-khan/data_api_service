from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Topic(Base):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Folder(Base):
    name = models.CharField(max_length=50)
    parent_id = models.IntegerField()

    def __str__(self):
        return self.name


class Document(Base):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    path = models.CharField(max_length=700)
    topics = models.ForeignKey(Topic, on_delete=models.CASCADE)
    folders = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
