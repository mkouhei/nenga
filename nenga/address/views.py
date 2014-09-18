# -*- coding: utf-8 -*-
""" views of nenga.address """
from django.shortcuts import render_to_response
from django.template import RequestContext
from nenga.address.models import Contact, PlanActual, Year

LATEST_YEAR = Year.objects.latest_year()


def index(request):
    """ index """
    return render_to_response('address/index.html',
                              {'is_authenticated':
                               request.user.is_authenticated(),
                               'year': LATEST_YEAR},
                              context_instance=RequestContext(request))


def contacts(request):
    """ list view of contacts """
    contacts = Contact.objects.owned_list(request.user)

    return render_to_response('address/contact_list.html',
                              {'is_authenticated':
                               request.user.is_authenticated(),
                               'year': LATEST_YEAR,
                               'contacts': contacts},
                              context_instance=RequestContext(request))


def plan_actual(request, year):
    """ list view of plan and actual """
    plan_actuals = PlanActual.objects.owned_list_by_year(request.user,
                                                         year)
    return render_to_response('address/plan_actual_list.html',
                              {'is_authenticated':
                               request.user.is_authenticated(),
                               'year': LATEST_YEAR,
                               'plan_actuals': plan_actuals},
                              context_instance=RequestContext(request))
