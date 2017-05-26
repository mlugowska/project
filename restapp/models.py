# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=True)
    carrot = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    completed = models.BooleanField(default=False)

    class Meta:
        # model = Profile
        ordering = ('name',) ## kolejność wyświetlania