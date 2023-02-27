from django.test import SimpleTestCase
from myapp.forms import DestinationForm

class TestForms(SimpleTestCase):
    
    def test_destination_form_valid_data(self):
        form = DestinationForm(data={
            'destination' : 'Tampa, FL, USA',
            'checkin' : '2023-02-22',
            'checkout' : '2023-03-01',
            'occasion' : 'birthday',
            'gender' : 'male',
        })
        self.assertTrue(form.is_valid())

    def test_destination_form_invalid_data(self):
        form = DestinationForm(data={
            'destination' : 'Tampa, FL, USA',
            'checkin' : 'badDate',
            'checkout' : 'badDate',
            'occasion' : 'birthday',
            'gender' : 'male',
        })

        self.assertFalse(form.is_valid())
    