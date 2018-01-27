from django.shortcuts import render, redirect
from django.urls import reverse

from modules.accounts.forms import (
    RegistrationForm,
    EditProfileForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from .serializers import UserSerializer, UserProfileSerializer
from .models import UserProfile
from rest_framework.views import APIView

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')

            user = authenticate(
                username=username,
                password=password
            )
            login(request,user)


            return redirect(reverse('home:home'))
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)

def view_profile( request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

def edit_profile( request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)



# ----------------------API---------------------------------

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



class UserDetailView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = User(user)
        return Response(serializer.data)

class UserProfileDetailView(APIView):
    def get(self, request, pk):
        userprofile = get_object_or_404(UserProfile, pk=pk)
        serializer = User(userprofile)
        return Response(serializer.data)





