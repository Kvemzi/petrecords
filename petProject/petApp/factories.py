import factory
from factory.django import DjangoModelFactory
from factory.faker import Faker
from factory.fuzzy import FuzzyText
from .models import PetSpecialist, Veterinary, Vaccination, Pet, PetVaccination, Consultation

class PetSpecialistFactory(DjangoModelFactory):
    class Meta:
        model = PetSpecialist

    name = Faker('name')
    specialization = factory.fuzzy.FuzzyChoice(['cat', 'dog', 'giraffe', 'snake', 'mouse', 'elephant'])

class VeterinaryFactory(DjangoModelFactory):
    class Meta:
        model = Veterinary

    name = Faker('name')
    email = Faker('email')
    phone_number = Faker('phone_number')
    address = Faker('street_address')
    pet_specialist = factory.SubFactory(PetSpecialistFactory)

class VaccinationFactory(DjangoModelFactory):
    class Meta:
        model = Vaccination

    name = Faker('word')
    description = Faker('paragraph')

class PetFactory(DjangoModelFactory):
    class Meta:
        model = Pet

    name = Faker('name')
    species = Faker('word')
    breed = factory.fuzzy.FuzzyChoice(['cat', 'dog', 'giraffe', 'snake', 'mouse', 'elephant'])
    age = factory.fuzzy.FuzzyInteger(0, 15)

class PetVaccinationFactory(DjangoModelFactory):
    class Meta:
        model = PetVaccination

    pet = factory.SubFactory(PetFactory)
    vaccination = factory.SubFactory(VaccinationFactory)

class ConsultationFactory(DjangoModelFactory):
    class Meta:
        model = Consultation

    pet = factory.SubFactory(PetFactory)
    veterinary = factory.SubFactory(VeterinaryFactory)
    date = Faker('date')
    description = Faker('paragraph')