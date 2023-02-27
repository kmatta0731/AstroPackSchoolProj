from django.test import TestCase
from occasion.models import * 

class TestModels(TestCase):
    '''
    def setUp(self):
        self.Essential = Essential.objects.create(
          Essentials =  'Essential 1',
          description = 'Essential Description',
          essentials_item_category = null,
          essentials_gender = null,
            
        )
    ''' 
    
    def test_gender_choice(self):
        self.gender1 = Gender.objects.create( gen = 'M')
        self.assertEquals(self.gender1.gen, 'M')

    ''' The below test SHOULD fail as it has a length > 1.
    def test_gender_choice_length(self):
        self.gender2 = Gender.objects.create(gen = 'SomeGender')
        self.assertEquals(self.gender2.gen, 'SomeGender')
    ''' 