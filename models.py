from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from base import models as base_models
# Create your models here.


class Calification(base_models.FullSlugBaseModel):
    """
    Generic Relationship example from https://docs.djangoproject.com/es/1.10/ref/contrib/contenttypes/#generic-relations
    """
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    rating = models.DecimalField(decimal_places=2, max_digits=3)
    opinion = models.TextField(blank=True)

    SLUG_RANDOM_CHARS = 20