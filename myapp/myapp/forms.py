# code for generator form on home page
from datetime import date, timedelta
from django import forms
from django.shortcuts import render, redirect

OCCASIONS = [
    ('', 'Choose an occasion'),
    (1, 'Wedding'),
    (2, 'Anniversary'),
    (3, 'Music Festival'),
    (4, 'Birthday'),
    (5, 'Business'),
    (6, 'Holidays'),
    (7, 'Leisure'),
]

GENDERS = [
    ('', "Gender (Optional)"),
    ('male', 'Male'),
    ('female', 'Female')
]

ACTIVITY_CHOICES = [
    (1, 'Beach'), 
    (2, 'Camping'), 
    (3, 'Hiking'), 
    (4, 'Skiing/Snowboarding')
]

class DestinationForm(forms.Form):
    destination = forms.CharField(widget=forms.TextInput(attrs={'id':'destination', 'placeholder': 'Enter destination'}))
    checkin = forms.DateField(initial=date.today(), widget=forms.DateInput(attrs={'type': 'date', 'class': 'date-input', 'id':'check-in-field'}))
    checkout = forms.DateField(initial=(date.today() + timedelta(days=7)),widget=forms.DateInput(attrs={'type': 'date', 'class': 'date-input'}))
    occasion = forms.CharField(widget=forms.Select(choices=OCCASIONS, attrs={'placeholder': 'Choose an occasion', 'class': 'occasion-dropdown'}))
    gender = forms.CharField(required=False,widget=forms.Select(choices=GENDERS, attrs={'placeholder': 'Choose an occasion', 'class': 'gender-dropdown'}))
    activities = forms.MultipleChoiceField(choices=ACTIVITY_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'id':'activity-checkbox'}))

    def clean(self):  # makes sure that checkout date is after checkin
        cleaned_data = super().clean()
        checkin = cleaned_data.get('checkin')
        checkout = cleaned_data.get('checkout')

        if checkin and checkout and checkin >= checkout:   
            raise forms.ValidationError("Check-in date must be before check-out date.")

def process_form(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            checkin = form.cleaned_data.get('checkin')
            checkout = form.cleaned_data.get('checkout')
            if checkout < checkin:
                form.add_error(
                    None, "Checkout date should be after check-in date"
                )
                return render(request, 'index.html', {'form': form})
            # process the form data here
            return redirect('saved_trips')
    else:
        form = DestinationForm()
    return render(request, 'index.html', {'form': form})