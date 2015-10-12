"""admin of Nenga as Django App."""
from django.contrib import admin
from nenga.address.models import Contact, Year, PlanActual, BackLayout


class PlanActualAdmin(admin.ModelAdmin):
    """Customizing list display for PlanActual."""

    list_display = ('destination', 'year', 'plan', 'actual')


class BackLayoutAdmin(admin.ModelAdmin):
    """Customizing list display for BackLayout."""

    list_display = ('year',)

admin.site.register(Contact)
admin.site.register(Year)
admin.site.register(BackLayout, BackLayoutAdmin)
admin.site.register(PlanActual, PlanActualAdmin)
