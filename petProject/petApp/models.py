from django.db import models

# Create your models here.
#3 Class methods for pets and Veterinary, which are connected at least with each of relation; one to one, one to many, many to many. These  methods are called Pet, Owner and Veterinary



class PetSpecialist(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

class Veterinary(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    pet_specialist = models.OneToOneField(PetSpecialist, on_delete=models.CASCADE)


class Vaccination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    vaccinations = models.ManyToManyField(Vaccination, through='PetVaccination')
class PetVaccination(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccination = models.ForeignKey(Vaccination, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('pet', 'vaccination')


class Consultation(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    veterinary = models.ForeignKey(Veterinary, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()


