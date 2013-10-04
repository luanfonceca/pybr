#!/usr/bin/env python
# encoding: utf-8

from django import template

register = template.Library()

@register.filter
def get_attr(obj, arg, default=None):
    result = getattr(obj, arg, default)
    if isinstance(result, (list, tuple)):
        result = ", ".join(result)
    return result