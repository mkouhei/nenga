# -*- coding: utf-8 -*-
""" models of nenga.address """
from django.db import models
from shortuuidfield import ShortUUIDField


class BaseObject(models.Model):
    """ Abstract base model that had id attribute formatted as shortuuid. """
    id = ShortUUIDField(primary_key=True, auto=True, verbose_name='UUID')

    class Meta(object):
        """ meta class of BaseObject """
        abstract = True


class Contact(BaseObject):
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
    postal_code = models.DecimalField(max_digits=7, decimal_places=0)
    prefecture = models.CharField(max_length=2, choices=PREFECTURE_CHOICES)
    city = models.CharField(max_length=256, unique=True)
    address = models.CharField(max_length=255, unique=False)
    address2 = models.CharField(max_length=255, unique=False,
                                blank=True, default="")
    patner_name = models.CharField(max_length=255, unique=False,
                                   blank=True, default="")

    class Meta(object):
        """ meta class of Contact """
        db_table = 'contact'
        unique_together = ('last_name', 'first_name', 'address', 'postal_code')

    def __unicode__(self):
        return "%s %s" % (self.last_name, self.first_name)


class PlanActual(BaseObject):
    """ plan and actual """
    destination = models.ForeignKey(Contact)
    year = models.DecimalField(max_digits=4, decimal_places=0)
    plan = models.BooleanField(default=True)
    actual = models.BooleanField(default=True)

    class Meta(object):
        """ meta class of PlanActual """
        db_table = 'plan_actual'
        unique_together = ('destination', 'year')

    def __unicode__(self):
        return self.destination
