# -*- coding: utf-8 -*-
""" views of nenga.address """
from django.shortcuts import render_to_response
from django.template import RequestContext
from nenga.address.models import Contact


def index(request):
    """ index """
    return render_to_response('address/index.html',
                              {'is_authenticated':
                               request.user.is_authenticated()},
                              context_instance=RequestContext(request))


def contacts(request):
    """ list view of contacts """
    contacts = Contact.objects.filter(owner=request.user)
    return render_to_response('address/contacts.html',
                              {'is_authenticated':
                               request.user.is_authenticated(),
                               'contacts': contacts},
                              context_instance=RequestContext(request))
