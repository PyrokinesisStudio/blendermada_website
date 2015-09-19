from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone


class Request(models.Model):

    name = models.CharField('Name', max_length=50)
    slug = models.SlugField('Slug')
    description = models.TextField('Description', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='requests', blank=True, null=True)
    date = models.DateTimeField('Date', default=timezone.now)
    closed = models.BooleanField('Closed', default=False)
    image = models.ImageField('')
    thumb = models.ImageField('')
