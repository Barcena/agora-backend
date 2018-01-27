from django.urls import path, include
from . import views # . will look into docs with the name views in this file this 
from django.contrib.auth.views import (
login, logout, 
password_reset, password_reset_done,
password_reset_confirm, password_reset_complete)# get login vi
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'v1/users/', views.UserViewSet),
router.register(r'v1/userprofiles/', views.UserProfileViewSet)



app_name = 'accounts'

	
urlpatterns = [
    path(r'login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path(r'logout/', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    path(r'register/', views.register, name='register'),
    path(r'profile/', views.view_profile, name='view_profile'),
    path(r'profile/<int:pk>/', views.view_profile, name='view_profile_with_pk'),
    path(r'profile/edit/', views.edit_profile, name='edit_profile'),
    path(r'change-password/', views.change_password, name='change_password'),

    path(r'reset-password/', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),

    path(r'reset-password/done/', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),

    path(r'reset-password/confirm/(<uidb64>[0-9A-Za-z]+)-(<token>.+)/', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),

    path(r'reset-password/complete/', password_reset_complete,{'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete'),
    
    path(r'api/', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api-detail/',views.UserDetailView )

]