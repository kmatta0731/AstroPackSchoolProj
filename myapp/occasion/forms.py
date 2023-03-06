from datetime import date, timedelta
from django import forms
from django.shortcuts import render, redirect

class UploadFileForm(forms.Form):
    file = forms.FileField()