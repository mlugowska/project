from rest_framework import serializers
from restapp.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    carrot = serializers.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    # completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        """
        Create and return a new `reastapp` instance, given the validated data.
        """
        return Profile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `restapp` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.carrot = validated_data.get('carrot', instance.carrot)
        instance.save()
        return instance