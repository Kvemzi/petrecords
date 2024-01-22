from django.db import models

# Create your models here.
from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    age = models.IntegerField()
    owner = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class VetService(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.pet.name} - {self.service_name}"