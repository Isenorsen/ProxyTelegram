from rest_framework import serializers
from .models import *


class ProxySerializer(serializers.HyperlinkedModelSerializer):
    """Serializer of our model"""
    class Meta:
        model = Proxy
        fields = ['channel_name',
                  'nickname',
                  'description',
                  'url',
                  'avatar',
                  'active']