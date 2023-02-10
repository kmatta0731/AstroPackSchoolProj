from django import forms
from django.shortcuts import render, redirect

class DestinationForm(forms.Form):
    destination = forms.CharField()
    checkin = forms.DateField()
    checkout = forms.DateField()

def process_form(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            # process the form data here
            # ...
            return redirect('success')
    else:
        form = DestinationForm()
    return render(request, 'index.html', {'form': form})
