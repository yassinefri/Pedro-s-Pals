from django.test import TestCase
from .models import PetProfile
from django.contrib.auth.models import User

class PetProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.pet = PetProfile.objects.create(
            owner=self.user,
            name='Buddy',
            age=3,
            species='Dog',
            breed='Golden Retriever',
            description='A friendly dog'
        )

    def test_pet_profile_creation(self):
        self.assertEqual(self.pet.name, 'Buddy')
        self.assertEqual(self.pet.age, 3)
        self.assertEqual(self.pet.species, 'Dog')
        self.assertEqual(self.pet.breed, 'Golden Retriever')
        self.assertEqual(self.pet.description, 'A friendly dog')
