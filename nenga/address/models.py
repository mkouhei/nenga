# -*- coding: utf-8 -*-
""" models of nenga.address """
from django.db import models
from django.db.models import Max
from django.db.models.query import QuerySet
from django.forms import ModelForm, HiddenInput
from django.contrib.auth.models import User
from shortuuidfield import ShortUUIDField
import jsonfield
from nenga.queryset.models import CustomQuerySetManager


class BaseObject(models.Model):
    """ Abstract base model that had id attribute formatted as shortuuid. """
    id = ShortUUIDField(primary_key=True, auto=True, verbose_name='UUID')

    class Meta(object):
        """ meta class of BaseObject """
        abstract = True


class PrivateObject(BaseObject):
    """ Abstract private model that extend with owner to BaseObject. """
    owner = models.ForeignKey(User, blank=False, null=True,
                              on_delete=models.SET_NULL)

    class Meta(object):
        """ meta class of PrivateObject """
        abstract = True

    class QuerySet(QuerySet):
        """ Override QuerySet """
        def owned_list(self, user):
            """ return owned list """
            return self.filter(owner=user)

        def owned_list_by_year(self, user, year):
            """ return owned list by year """
            return self.filter(owner=user).filter(year__year=year)


class Contact(PrivateObject):
    """ Contact model """
    PREFECTURE_CHOICES = [
        ('01', '北海道'),
        ('02', '青森県'),
        ('03', '岩手県'),
        ('04', '宮城県'),
        ('05', '秋田県'),
        ('06', '山形県'),
        ('07', '福島県'),
        ('08', '茨城県'),
        ('09', '栃木県'),
        ('10', '群馬県'),
        ('11', '埼玉県'),
        ('12', '千葉県'),
        ('13', '東京都'),
        ('14', '神奈川県'),
        ('15', '新潟県'),
        ('16', '富山県'),
        ('17', '石川県'),
        ('18', '福井県'),
        ('19', '山梨県'),
        ('20', '長野県'),
        ('21', '岐阜県'),
        ('22', '静岡県'),
        ('23', '愛知県'),
        ('24', '三重県'),
        ('25', '滋賀県'),
        ('26', '京都府'),
        ('27', '大阪府'),
        ('28', '兵庫県'),
        ('29', '奈良県'),
        ('30', '和歌山県'),
        ('31', '鳥取県'),
        ('32', '島根県'),
        ('33', '岡山県'),
        ('34', '広島県'),
        ('35', '山口県'),
        ('36', '徳島県'),
        ('37', '香川県'),
        ('38', '愛媛県'),
        ('39', '高知県'),
        ('40', '福岡県'),
        ('41', '佐賀県'),
        ('42', '長崎県'),
        ('43', '熊本県'),
        ('44', '大分県'),
        ('45', '宮崎県'),
        ('46', '鹿児島県'),
        ('47', '沖縄県')]
    last_name = models.CharField(max_length=255, unique=False)
    first_name = models.CharField(max_length=255, unique=False)
    zip_code = models.CharField(max_length=7, blank=False)
    prefecture = models.CharField(max_length=2, choices=PREFECTURE_CHOICES)
    city = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, unique=False)
    address2 = models.CharField(max_length=255, unique=False,
                                blank=True, default="")
    patner_name = models.CharField(max_length=255, unique=False,
                                   blank=True, default="")
    objects = CustomQuerySetManager()

    class Meta(object):
        """ meta class of Contact """
        db_table = 'contact'
        unique_together = ('last_name', 'first_name', 'address', 'zip_code')
        permissions = (
            ('view_contact', 'View contact'),
            )

    def __unicode__(self):
        return "%s %s" % (self.last_name, self.first_name)


class Year(models.Model):
    """ Year """
    year = models.DecimalField(max_digits=4, decimal_places=0, unique=True)
    objects = CustomQuerySetManager()

    class Meta(object):
        """ meta class of Year """
        db_table = 'year'

    def __unicode__(self):
        return unicode(self.year)

    class QuerySet(QuerySet):
        """ Override QuerySet """
        def latest_year(self):
            """ return latest record """
            return self.aggregate(Max('year'))


class PlanActual(PrivateObject):
    """ plan and actual """
    destination = models.ForeignKey(Contact)
    year = models.ForeignKey(Year)
    plan = models.BooleanField(default=True)
    actual = models.NullBooleanField(default=None)
    objects = CustomQuerySetManager()

    class Meta(object):
        """ meta class of PlanActual """
        db_table = 'plan_actual'
        unique_together = ('destination', 'year')
        permissions = (
            ('view_plan_actual', 'View PlanActual'),
            )

    def __unicode__(self):
        return unicode(self.destination)


class BackLayout(PrivateObject):
    """ Back layout AKA "Ura-men" """
    year = models.ForeignKey(Year)
    layout_template = models.TextField()
    template_attributes = jsonfield.JSONField()

    class Meta(object):
        """ meta class of BackLayout """
        db_table = 'back_layout'
        unique_together = ('year',)
        permissions = (
            ('view_back_layout', 'View BackLayout'),
            )

    def __unicode__(self):
        return unicode(self.year)
