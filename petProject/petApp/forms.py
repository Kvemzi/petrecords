# forms.py
from django import forms
from .models import Pet, Veterinary, PetSpecialist, Vaccination, Consultation, PetVaccination

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'species', 'breed', 'age')

class VeterinaryForm(forms.ModelForm):
    class Meta:
        model = Veterinary
        fields = ('name', 'email', 'phone_number', 'address','pet_specialist')

class PetSpecialistForm(forms.ModelForm):
    class Meta:
        model = PetSpecialist
        fields = ('name', 'specialization')

class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ('name', 'description')

class ConsultationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    pet = forms.ModelChoiceField(queryset=Pet.objects.all(), empty_label="Select Pet")
    veterinary = forms.ModelChoiceField(queryset=Veterinary.objects.all(), empty_label="Select Veterinary")

    class Meta:
        model = Consultation
        fields = ('pet', 'veterinary', 'date', 'description')
        

class AddVaccinationForm(forms.ModelForm):

    class Meta:

        model = PetVaccination

        fields = ('vaccination',)