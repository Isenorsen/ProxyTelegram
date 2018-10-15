from django.db import models

# Create your models here.

class Proxy(models.Model):
    channel_name = models.CharField(max_length=100, verbose_name='Название канала')
    nickname = models.CharField(max_length=100, default=None, verbose_name='Ник канала')
    description = models.TextField(default=None, verbose_name='Описание')
    url = models.CharField(max_length=200, default=None, verbose_name='Ссылка')
    avatar = models.ImageField(upload_to='attachments', default=None, verbose_name='Аватар')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.channel_name