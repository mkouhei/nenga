""" admin of Nenga as Django App """
from django.contrib import admin
from nenga.address.models import Contact, PlanActual

admin.site.register(Contact)
admin.site.register(PlanActual)
