""" admin of Nenga as Django App """
from django.contrib import admin
from nenga.address.models import Contact, PlanActual


class PlanActualAdmin(admin.ModelAdmin):
    """ Customizing list display for PlanActual """
    list_display = ('destination', 'year', 'plan', 'actual')

admin.site.register(Contact)
admin.site.register(PlanActual, PlanActualAdmin)
