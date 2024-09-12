from django.core.management.base import BaseCommand
from petApp.factories import PetSpecialistFactory, VeterinaryFactory, VaccinationFactory, PetFactory, PetVaccinationFactory, ConsultationFactory

class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(7):
            pet_specialist = PetSpecialistFactory()
            print(f"Created pet specialist: {pet_specialist.name}")

        for _ in range(7):
            veterinary = VeterinaryFactory()
            print(f"Created veterinary: {veterinary.name}")

        for _ in range(50):
            vaccination = VaccinationFactory()
            print(f"Created vaccination: {vaccination.name}")

        for _ in range(50):
            pet = PetFactory()
            print(f"Created pet: {pet.name}")

        for _ in range(50):
            pet_vaccination = PetVaccinationFactory()
            print(f"Created pet vaccination: {pet_vaccination.pet.name} - {pet_vaccination.vaccination.name}")

        for _ in range(50):
            consultation = ConsultationFactory()
            print(f"Created consultation: {consultation.pet.name} - {consultation.veterinary.name}")