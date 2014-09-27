# -*- coding: utf-8 -*-
""" forms of nenga.address """
from django.forms import ModelForm, HiddenInput
from nenga.address.models import Contact


class ContactForm(ModelForm):
    """ ModelForm of Contact """
    class Meta(object):
        """ meta class of ContactForm """
        model = Contact
        fields = ('last_name',
                  'first_name',
                  'zip_code',
                  'prefecture',
                  'city',
                  'address',
                  'address2',
                  'partner_name',
                  'owner')

        widgets = {'owner': HiddenInput()}
