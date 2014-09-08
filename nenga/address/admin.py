""" admin of Nenga as Django App """
from django.contrib import admin
from nenga.address.models import Contact

admin.site.register(Contact)
