from django.db import models

# Create your models here.

class Proxy(models.Model):
    channel_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, default=None)
    description = models.TextField(default=None)
    url = models.CharField(max_length=200, default=None)
    avatar = models.ImageField(upload_to='attachments', default=None)

    def __str__(self):
        return self.channel_name