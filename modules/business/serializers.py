from django.conf.urls import url, include
from .models import B2cProfile
from rest_framework import routers, serializers, viewsets

class B2cProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = B2cProfile
        fields = ( 'pk','business_name','description', 'location', 'website', 'phone', 'apertura', 'cierre', 'slug', 'category',  )

