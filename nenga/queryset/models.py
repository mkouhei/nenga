# -*- coding: utf-8 -*-
""" Custom QuerySet models """
from django.db import models


class CustomQuerySetManager(models.Manager):
    """ A re-usable Manager to access a custom QuerySet.
    This snippet's origin is stackoverflow.
    http://stackoverflow.com/questions/2163151/\
    custom-queryset-and-manager-without-breaking-dry
    """
    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_query_set(), attr, *args)

    def get_queryset(self):
        """ override get_queryset """
        return self.model.QuerySet(self.model)
