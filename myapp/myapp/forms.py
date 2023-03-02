# code for generator form on home page
from datetime import date, timedelta
from django import forms
from django.shortcuts import render, redirect

OCCASIONS = [
    ('', 'Choose an occasion'),
    ('wedding', 'Wedding'),
    ('anniversary', 'Anniversary'),
    ('music_festival', 'Music Festival'),
    ('birthday', 'Birthday'),
    ('business', 'Business'),
    ('holidays', 'Holidays'),
    ('no_reason', 'Leisure'),
]

GENDERS = [
    ('', "Gender (Optional)"),
    ('male', 'Male'),
    ('female', 'Female')
]

class DestinationForm(forms.Form):
    destination = forms.CharField(widget=forms.TextInput(attrs={'id':'destination', 'placeholder': 'Enter destination'}))
    checkin = forms.DateField(initial=date.today(), widget=forms.DateInput(attrs={'type': 'date', 'class': 'date-input', 'id':'check-in-field'}))
    checkout = forms.DateField(initial=(date.today() + timedelta(days=7)),widget=forms.DateInput(attrs={'type': 'date', 'class': 'date-input'}))
    occasion = forms.CharField(widget=forms.Select(choices=OCCASIONS, attrs={'placeholder': 'Choose an occasion', 'class': 'occasion-dropdown'}))
    activities = forms.MultipleChoiceField(choices=[('beach', 'Beach'), ('camping', 'Camping'), ('hiking', 'Hiking'), ('skiing', 'Skiing/Snowboarding')])
    gender = forms.CharField(required=False,widget=forms.Select(choices=GENDERS, attrs={'placeholder': 'Choose an occasion', 'class': 'gender-dropdown'}))

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