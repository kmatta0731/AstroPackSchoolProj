# code for generator form on home page
from django import forms
from django.shortcuts import render, redirect

class DestinationForm(forms.Form):
    destination = forms.CharField(widget=forms.TextInput(attrs={'id':'destination', 'placeholder': 'Enter destination'}))
    checkin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'date-input'}))
    checkout = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'date-input'}))

    def clean(self):
        cleaned_data = super().clean()
        checkin = cleaned_data.get('checkin')
        checkout = cleaned_data.get('checkout')

        if checkin and checkout and checkin >= checkout:    # makes sure that checkout date is after checkin
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
            return redirect('home')
    else:
        form = DestinationForm()
    return render(request, 'index.html', {'form': form})