# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=True)
    carrots = models.IntegerField(default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)])

    # class Meta:
    #     ordering = ('carrots',) ## kolejność wyświetlania

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs) # Call the "real" save() method
    # to ensure that the object still gets saved into the database. If you forget to call the superclass method, the default behavior won’t happen and the database won’t get touched.
    # It’s also important that you pass through the arguments that can be passed to the model method – that’s what the *args, **kwargs bit does. Django will, from time to time, extend the capabilities of built-in model methods, adding new arguments. If you use *args, **kwargs in your method definitions, you are guaranteed that your code will automatically support those arguments when they are added.