from django.contrib import admin
from .models import appointment,contact,pricing,dentist,review

# Register your models here.

admin.site.register(appointment)
admin.site.register(contact)
admin.site.register(pricing)
admin.site.register(dentist)
admin.site.register(review)
