from django.contrib import admin
from .models import Cliente, Modality, DBVersion, AnatomicalRegion, AnatomyImage, Answer, Assignment, Question

admin.site.register(Cliente)
admin.site.register(Modality)
admin.site.register(DBVersion)
admin.site.register(AnatomicalRegion)
admin.site.register(AnatomyImage)
admin.site.register(Answer)
admin.site.register(Assignment)
admin.site.register(Question)
