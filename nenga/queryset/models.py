# -*- coding: utf-8 -*-
"""Custom QuerySet models."""
from django.db.models import Max
from django.db.models.query import QuerySet


class PrivateQuerySet(QuerySet):

    """Override QuerySet."""

    def owned_list(self, user):
        """return owned list."""
        return self.filter(owner=user)

    def owned_list_by_year(self, user, year):
        """return owned list by year."""
        return self.filter(owner=user).filter(year__year=year)


class YearQuerySet(QuerySet):

    """Override QuerySet."""

    def latest_year(self):
        """return latest record."""
        return self.aggregate(Max('year'))
