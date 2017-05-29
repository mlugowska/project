# -*- coding: utf-8 -*-
from rest_framework import serializers
from restapp.models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('url', 'id', 'name', 'carrots')


