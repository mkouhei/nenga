# -*- coding: utf-8 -*-
""" views of nenga.address """
from django.shortcuts import render_to_response
from django.template import RequestContext
from nenga.address.models import Contact, PlanActual, Year


def index(request):
    """ index """
    return render_to_response('address/index.html',
                              {'is_authenticated':
                               request.user.is_authenticated()},
                              context_instance=RequestContext(request))


def contacts(request):
    """ list view of contacts """
    contacts = Contact.objects.owned_list(request.user)

    return render_to_response('address/contact_list.html',
                              {'is_authenticated':
                               request.user.is_authenticated(),
                               'contacts': contacts},
                              context_instance=RequestContext(request))


def plan_actual(request, year=None):
    """ list view of plan and actual """
    years = Year.objects.all()
    if year:
        plan_actuals = PlanActual.objects.owned_list_by_year(request.user,
                                                             year)
    else:
        plan_actuals = PlanActual.objects.owned_list(request.user)
    return render_to_response('address/plan_actual_list.html',
                              {'is_authenticated':
                               request.user.is_authenticated(),
                               'years': years,
                               'plan_actuals': plan_actuals},
                              context_instance=RequestContext(request))
