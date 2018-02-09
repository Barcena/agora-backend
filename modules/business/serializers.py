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

    base64_image = SerializerMethodField()
    # image = SerializerMethodField()

    class Meta:
        model = B2cProfile
        fields = ( 
            'owner',
            'pk', 
            'business_name',
            'description', 
            'location', 
            'website', 
            'phone', 'apertura', 
            'cierre', 
            'slug', 
            'category', 
            'base64_image', )
        
    def get_base64_image(self, obj):
        f = open(obj.image.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data



    # def get_image(self, obj):
    #     try:
    #         image = obj.image.url
    #     except:
    #         image = None
    #     return image