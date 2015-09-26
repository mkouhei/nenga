# -*- coding: utf-8 -*-
"""basic routing of Nenga as Django App."""
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', RedirectView.as_view(url='/nenga/')),
                       (r'^login/$', 'django.contrib.auth.views.login',
                        {'template_name': 'address/login.html'}),
                       (r'^logout/$', 'django.contrib.auth.views.logout',
                        {'template_name': 'address/logout.html'}),
                       (r'^nenga/', include('nenga.address.urls')),
                       url(r'^admin/', include(admin.site.urls)),)
