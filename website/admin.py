from django.contrib import admin
from .models import appointments
from .models import contact

# Register your models here.

admin.site.register(appointments)
admin.site.register(contact)
