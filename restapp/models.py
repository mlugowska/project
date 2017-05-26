# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from pygments import highlight

class Profile(models.Model):
    # name = models.CharField(max_length=100, blank=True)
    carrots = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])

    # class Meta:
    #     # model = Profile
    #     ordering = ('carrot',) ## kolejność wyświetlania

    owner = models.ForeignKey('auth.User', related_name='profiles', on_delete=models.CASCADE)
    highlighted = models.TextField()


def save(self, *args, **kwargs):
    self.highlighted = highlight(self.code)
    super(Profile, self).save(*args, **kwargs)