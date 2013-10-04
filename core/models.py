from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from hstore_flattenfields.models import *

class PublishingHouse(DynamicFieldGroup):
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('core_publishinghouse_detail', (), {'pk': self.pk})


class Author(HStoreM2MGroupedModel):
    publishing_houses = models.ManyToManyField(
        to=PublishingHouse, 
        null=True, 
        blank=True, 
        related_name='authors', 
        verbose_name='Publishing House'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )
    
    class Meta:
        # hstore
        hstore_related_field = 'publishing_houses'

    @models.permalink
    def get_absolute_url(self):
        return ('core_author_detail', (), {'pk': self.pk})


class Book(HStoreModel):
    author = models.ForeignKey(
        to=Author, 
        null=True, 
        blank=True,
        verbose_name='Author'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        default=now(),
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        default=now(),
        editable=False,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('core_book_detail', (), {'pk': self.pk})
