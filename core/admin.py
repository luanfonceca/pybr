#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin

from core.models import *

admin.site.register(PublishingHouse)
admin.site.register(Author)
admin.site.register(Book)
