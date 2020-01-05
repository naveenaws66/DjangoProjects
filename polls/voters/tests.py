from django.test import TestCase

from .models import people

class PeopleModelTest(TestCase):

    def setUp(self):
        people.objects.create(name='testingPeopleModel', phone='1234567')
    
    def test_people_content(self):
        voter = people.objects.get(id=1)
        expected_object_name = f'{voter.name}'
        expected_object_phone = f'{voter.phone}'
        self.assertEqual(expected_object_name, 'testingPeopleModel')
        self.assertEqual(expected_object_phone, '1234567')


