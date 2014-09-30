# -*- coding: utf-8 -*-
""" routing of nenga.address """
from django.conf.urls import patterns, url


urlpatterns = patterns('nenga.address.views',
                       url(r'^$', 'index', name='index'),
                       url(r'^profile/$', 'profile', name='profile'),
                       url(r'^contacts$', 'contacts', name='contacts'),
                       url(r'^contacts/(?P<pk>\w+)/$', 'contact_edit',
                           name='contact_edit'),
                       url(r'^plan_actual/$', 'plan_actual',
                           name='plan_actual'),
                       url(r'^plan_actual/(?P<year>\d{4})/$', 'plan_actual',
                           name='plan_actuals'),
                       url(r'^plan_actual/(?P<pk>\w+)/$',
                           'plan_actual_edit',
                           name='plan_actual_edit'),)
