# -*- coding: utf-8 -*-
from restapp.models import Profile
from restapp.serializers import ProfileSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from restapp.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import detail_route


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     List of users and details about each of them
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    """
    List of existing profiles - a new can be added, existing (under URL) can be updated/deleted
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        profile = self.get_object()
        return Response(profile.highlighted)
    #
    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)





