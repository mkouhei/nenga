# -*- coding: utf-8 -*-
""" routing of nenga.address """
from django.conf.urls import patterns, url


urlpatterns = patterns('nenga.address.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^contacts$', 'contacts', name='contacts'),)
