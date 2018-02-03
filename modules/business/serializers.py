from django.core.files import File
import base64
from django.conf.urls import url, include
from .models import B2cProfile
from rest_framework import routers, serializers, viewsets
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )

class B2cProfileSerializer(serializers.ModelSerializer):

    image = SerializerMethodField()

    class Meta:
        model = B2cProfile
        fields = ( 
            'pk', 
        
            'business_name',
            'description', 
            'location', 
            'website', 
            'phone', 'apertura', 
            'cierre', 
            'slug', 
            'category',
            'image' ,
             )

    

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image