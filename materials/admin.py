from django.contrib import admin
from historicalarchives.materials.models import Material, Collection, Request_for_materials

django.site.register(Material)
django.site.register(Collection)
django.site.register(Request_for_materials)
