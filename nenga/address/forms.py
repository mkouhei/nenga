# -*- coding: utf-8 -*-
""" forms of nenga.address """
from django.forms import ModelForm, HiddenInput
from nenga.address.models import Contact


class ContactForm(ModelForm):
    """ ModelForm of Contact """
    class Meta(object):
        """ meta class of ContactForm """
        model = Contact
        widgets = {'owner': HiddenInput()}
