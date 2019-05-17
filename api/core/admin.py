from django.contrib import admin
from .models import Cliente, Modality, DBVersion

admin.site.register(Cliente)
admin.site.register(Modality)
admin.site.register(DBVersion)