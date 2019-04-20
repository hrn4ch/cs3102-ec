import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Topic(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    imageURL = models.URLField(default="https://www.templaza.com/blog/components/com_easyblog/themes/wireframe/images/placeholder-image.png")
    postURL = models.CharField(max_length=50, default="#")

    class Meta:
        ordering = ["title"]