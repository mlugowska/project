# -*- coding: utf-8 -*-
from rest_framework import serializers
from restapp.models import Profile


class ProfileSerializer(serializers.ModelSerializer):


    class Meta: # anything that’s not a field
        model = Profile # model name created to store profile
        fields = ('url', 'id', 'name', 'carrots')


