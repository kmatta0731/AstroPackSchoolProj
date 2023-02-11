from django.shortcuts import render
from .login import login_view
from .register import register_view
from .forms import process_form
from user_dashboard.views import dashboard
from .logout import logout_view
from django import forms
from .forms import DestinationForm

# class DestinationForm(forms.Form):
#     destination = forms.CharField()
#     checkin = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Check-in'}))
#     checkout = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Check-out'}))

def home(request):
    return render(request, 'index.html', {'form': DestinationForm})
