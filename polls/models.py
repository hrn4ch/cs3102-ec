import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Topic(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    image = models.ImageField(default='media/default-thumbnail.jpg')
    postURL = models.CharField(max_length=50, default="#")

    class Meta:
        ordering = ["title"]