# -*- coding: utf-8 -*-
""" views of nenga.address """
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    """ index """
    return render_to_response('address/index.html',
                              {'is_authenticated':
                               request.user.is_authenticated()},
                              context_instance=RequestContext(request))
