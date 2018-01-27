from django.urls import path, include

from . import views
from .views import ( 
B2cDetailsView,
BusinessCreateView,
BusinessUpdateView,
B2cApiDetailsView
	)
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'v1/b2cprofiles', views.B2cProfileViewSet),
# router.register(r'b2c/<int:pk>/', views.B2cApiDetailsView)

app_name = 'business'

urlpatterns = [
	path(r'b2c/register/', views.register, name='register'),
	path(r'b2c/create/', BusinessCreateView.as_view(), name='create'),
	path(r'b2c-profile/', views.view_b2c_profile, name='view_profile'),
    path('<slug:slug>/', views.B2cDetailsView.as_view(), name='detail'),
    path(r'<slug:slug>/edit/', BusinessUpdateView.as_view(), name='edit'),
    path(r'api/', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/<int:pk>/', views.B2cApiDetailsView),
   ]