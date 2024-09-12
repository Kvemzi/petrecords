import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "petProject.settings")
django.setup()


from petApp.factories import PetFactory, VeterinaryFactory, PetSpecialistFactory, VaccinationFactory, ConsultationFactory, PetVaccinationFactory

pets = PetFactory.create_batch(50)
veterinaries = VeterinaryFactory.create_batch(7)
pet_specialists = PetSpecialistFactory.create_batch(7)
vaccinations = VaccinationFactory.create_batch(25)
consultations = ConsultationFactory.create_batch(75)
pet_vaccinations = PetVaccinationFactory.create_batch(35)