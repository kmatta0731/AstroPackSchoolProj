from django.test import TestCase, Client
from django.urls import reverse
from occasion.models import *
import json

class TestViews(TestCase):
    
    def setUp(self): #Set up a certain scenario prior to testing.
        self.client = Client()
        self.home_url = reverse('home')
        self.login_url = reverse('login')
        '''Testing out a table from models.py
        self.gender1 = Gender.objects.create(
             gen = 'M'
        )'''
        
    def test_home_GET(self):
        #Use line 16 and 17 if setUp is not created.
        #client = Client()
        #response = self.client.get(reverse('home')) #refer to the first parameter for home in urls.py
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200) # 200 means accessed the home properly
        self.assertTemplateUsed(response, 'index.html')

    def test_login_GET(self):
            response = self.client.get(self.login_url)

            self.assertEquals(response.status_code, 200) 
            self.assertTemplateUsed(response, 'login.html')
