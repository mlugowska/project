# -*- coding: utf-8 -*-
from restapp.models import Profile
from restapp.serializers import ProfileSerializer
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.response import Response


class ProfileViewSet(viewsets.ModelViewSet):

    """
    ADD, UPDATE OR DELETE RABBIT PROFILE
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self):
        profile = self.get_object()
        return Response(profile.highlighted)

    def perform_create(self, serializer):
        serializer.save()



