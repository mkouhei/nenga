# -*- coding: utf-8 -*-
""" views of nenga.address """
from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from nenga.address.models import Contact, PlanActual, Year
from nenga.address.forms import ContactForm, PlanActualForm


def index(request):
    """ index """
    return render_to_response('address/index.html',
                              {'is_authenticated':
                               request.user.is_authenticated()},
                              context_instance=RequestContext(request))


def profile(request):
    """ profile """
    return render_to_response('address/profile_detail.html',
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


def contact_edit(request, pk):
    """ edit view of contact """
    ContactFormSet = modelformset_factory(
        model=Contact,
        form=ContactForm)
    if request.method == 'POST':
        formset = ContactFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/nenga/contacts')
    else:
        formset = modelformset_factory(
            model=Contact,
            form=ContactForm,
            max_num=1,
            extra=1,
            )(queryset=Contact.objects.filter(id=pk))

    return render_to_response('address/contact_edit.html',
                              {'is_authenticated':
                               request.user.is_authenticated(),
                               'formset': formset},
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


def plan_actual_edit(request, pk):
    """ edit view of plan_actual """
    PlanActualFormSet = modelformset_factory(
        model=PlanActual,
        form=PlanActualForm)
    if request.method == 'POST':
        formset = PlanActualFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/nenga/plan_actual/')
    else:
        formset = modelformset_factory(
            model=PlanActual,
            form=PlanActualForm,
            max_num=1,
            extra=1,
        )(queryset=PlanActual.objects.filter(id=pk))

    return render_to_response('address/plan_actual_edit.html',
                              {'is_authenticated':
                               request.user.is_authenticated(),
                               'formset': formset},
                              context_instance=RequestContext(request))
