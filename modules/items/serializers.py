from django.conf.urls import url, include
from .models import Item
from rest_framework import routers, serializers, viewsets

class ItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ( 'pk', 'description', 'politicas', 'extra_info', 'price', 'timestamp' )