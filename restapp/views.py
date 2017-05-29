# -*- coding: utf-8 -*-
from restapp.models import Profile
from restapp.serializers import ProfileSerializer
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework.response import Response


class ProfileViewSet(viewsets.ModelViewSet):

    """
    ADD, UPDATE OR DELETE RABBIT PROFILE
    """

    #  API endpoint that allows users to be viewed or edited
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
# decorator can be used to add any custom endpoints that don't fit into the standard create/update/delete style.
    @detail_route()
    def highlight(self, *args, **kwargs):
        profile = self.get_object()
        return Response(profile.highlighted)

    def perform_create(self, serializer):
        serializer.save()
