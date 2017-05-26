from rest_framework import serializers
from restapp.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='profile-highlight', format='html')

    class Meta:
        model = Profile
        fields = ('url', 'id', 'owner', 'carrots')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profiles = serializers.HyperlinkedRelatedField(many=True, view_name='profile-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'profiles')