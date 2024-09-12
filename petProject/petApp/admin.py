# admin.py
from django.contrib import admin
from .models import Pet, PetVaccination, Vaccination, PetSpecialist, Veterinary, Consultation

class PetSpecialistAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')

class VeterinaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address')

class VaccinationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'age')

class PetVaccinationAdmin(admin.ModelAdmin):
    list_display = ('pet', 'vaccination')
    list_filter = ('pet', 'vaccination')

class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('pet', 'veterinary', 'date')
    list_filter = ('pet', 'veterinary')

admin.site.register(PetSpecialist, PetSpecialistAdmin)
admin.site.register(Veterinary, VeterinaryAdmin)
admin.site.register(Vaccination, VaccinationAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(PetVaccination, PetVaccinationAdmin)
admin.site.register(Consultation, ConsultationAdmin)