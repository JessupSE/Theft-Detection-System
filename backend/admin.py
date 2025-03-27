from django.contrib import admin
from .models import Alert, MediaFile, KnownPerson

admin.site.register(Alert)
admin.site.register(MediaFile)
admin.site.register(KnownPerson)

