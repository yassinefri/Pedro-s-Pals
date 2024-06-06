from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class PetProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='pet_photos/', blank=True, null=True)

    def __str__(self):
        return self.name