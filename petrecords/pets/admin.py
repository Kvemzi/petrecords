from django.contrib import admin
from .models import Pet, VetService

admin.site.register(Pet)
admin.site.register(VetService)