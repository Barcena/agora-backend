from django.urls import path, include
from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView,
    ItemsViewSet

)

from . import views

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'v1/items/', views.ItemsViewSet)


app_name = 'items'
urlpatterns = [
    path(r'create/',  ItemCreateView.as_view(), name='create'),
    path(r'<int:pk>/edit/', ItemUpdateView.as_view(), name='edit'),
    path(r'<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path(r'', ItemListView.as_view(), name='list'),
    path(r'api/', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]