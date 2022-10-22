from django.conf import settings
from django.db import models
from django.core.validators import *


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=900)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
    label = models.ForeignKey('Label', on_delete=models.SET_NULL, null=True)


class Label(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )
