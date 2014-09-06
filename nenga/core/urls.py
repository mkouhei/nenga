# -*- coding: utf-8 -*-
""" basic routing of Nenga as Django App """
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('', url(r'^admin/', include(admin.site.urls)),)
