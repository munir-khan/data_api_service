from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Folders(Base):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=700, default=None)

    def __str__(self):
        return self.path


class Topics(Base):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Documents(Base):
    name = models.CharField(max_length=50)
    folder = models.ForeignKey(Folders, related_name="folder_documents", on_delete=models.CASCADE, default=None)
    topic = models.ForeignKey(Topics, related_name="topic_documents", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
