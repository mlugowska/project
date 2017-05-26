# -*- coding: utf-8 -*-
from restapp.models import Profile
from restapp.serializers import ProfileSerializer
from rest_framework import generics

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer