# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.test import APITestCase
from restapp.models import Profile
from restapp.serializers import ProfileSerializer
from rest_framework import status
from django.core.urlresolvers import reverse
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


#####################################################################
# CREATING REQUIRED OBJECT to test whether the created object details match or not
# TESTING THE SERIALIZERS

class ProfileTest(APITestCase):
    def setUp(self):
        self.profile = Profile.objects.create(name='Frank', carrots=47)

    def test_profile_valid(self):
        profile = ProfileSerializer(data={'name': 'Pat', 'carrots': 8})
        self.assertTrue(profile.is_valid())
        print "A profile is valid"

######################################################################
# TESTING THE VIEWS


class AddProfileTest(APITestCase):
    def setUp(self):
        self.profile = Profile.objects.create(name='Frank', carrots=47)
        self.data = {'name': 'Pat', 'carrots': 9}

    def test_add_new_profile(self):
        response = self.client.post(reverse('profile-list'), self.data) # '/Get_profile_list/'
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print 'A new profile instance was CREATED'


class ReadProfileTest(APITestCase):
    def setUp(self):
        self.profile = Profile.objects.create(name='Frank', carrots=47)
        self.data = {'name': 'Pat', 'carrots': 8}
        self.name = Profile.objects.create(name='Karl')

    def test_read_profile_list(self):
        response = self.client.get(reverse('profile-list')) # '/Get_profile_list/'
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print 'A profile list was READED'

    def test_read_profile_detail(self):
        response = self.client.get(reverse('profile-detail', args=[self.profile.id])) # '# /Get_profile_list/2 -> id'
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print 'A profile detail was READED'


class UpdateProfileTest(APITestCase):
    def setUp(self):
        self.profile = Profile.objects.create(name='Frank', carrots=47)

        factory = APIRequestFactory()
        request = factory.get('/')

        serializer_context = {
            'request': Request(request),
        }

        self.data = ProfileSerializer(self.profile, context=serializer_context).data
        self.data.update({'name': 'Changed'})

    def test_update_profile(self):
        response = self.client.put(reverse('profile-detail', args=[self.profile.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print 'A profile was UPDATED'


class DeleteProfileTest(APITestCase):
    def setUp(self):
        self.profile = Profile.objects.create(name='Frank', carrots=47)
        self.data = {'name': 'Pat', 'carrots': 8}
        self.name = Profile.objects.create(name='Frank')

    def test_delete_profile(self):
        response = self.client.delete(reverse('profile-detail', args=[self.profile.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print 'A profile was DELETED'



