from django.contrib import admin
from materials.models import Material, Collection, Request_for_materials

admin.site.register(Material)
admin.site.register(Collection)
admin.site.register(Request_for_materials)
