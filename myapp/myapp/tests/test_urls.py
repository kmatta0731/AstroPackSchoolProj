from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import *

class TestUrls(SimpleTestCase): #SimpleTestCase when not interacting with database
    
    def test_login_url_is_resolved(self):
        url = reverse('login')
        #print(resolve(url)) # to see the ResolverMatch Object
        self.assertEquals(resolve(url).func, login_view) #Make sure that resolve url == ResolverMatch when line 9 on unit tests

    def test_register_url_is_resolved(self):
          url = reverse('register')
          self.assertEquals(resolve(url).func, register_view) 

    def test_home_url_is_resolved(self):
          url = reverse('home')
          self.assertEquals(resolve(url).func, home) 

    def test_process_form_url_is_resolved(self):
          url = reverse('process_form')
          self.assertEquals(resolve(url).func, process_form) 

    def test_dashboard_url_is_resolved(self):
          url = reverse('dashboard')
          self.assertEquals(resolve(url).func, dashboard) 

    def test_logout_url_is_resolved(self):
          url = reverse('logout')
          self.assertEquals(resolve(url).func, logout_view) 

    def test_process_data_url_is_resolved(self):
          url = reverse('process_data')
          self.assertEquals(resolve(url).func, process_data)

    def test_items_url_is_resolved(self):
          url = reverse('items')
          self.assertEquals(resolve(url).func, items)  