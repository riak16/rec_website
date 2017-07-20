from django import forms
from django.template.defaultfilters import mark_safe
from django.forms.formsets import BaseFormSet

from .models import Chronicle
from homepage.models import Info


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('name','rollno','mobileno','email')
        fields_required = ('name','rollno','mobileno','email')

    def __init__(self, *args, **kwargs):
        super(InfoForm, self).__init__(*args, **kwargs)
        self.fields['name'].label     = "Your name"
        self.fields['email'].label    = "Your E-mail"
        self.fields['rollno'].label   = "Your Roll No"
        self.fields['mobileno'].label = "Your Mobile No"
        #self.fields['captcha'].label = "Please prove you're not a robot"

class ChronicleForms(forms.ModelForm):
    class Meta:
        model = Chronicle
        fields = ('q1','q2','q3')
        fields_required = ('q1','q2','q3')

    def __init__(self, *args, **kwargs):
        super(ChronicleForms, self).__init__(*args, **kwargs)
        self.fields['q1'].label     = "Question 1 goes here"
        self.fields['q2'].label     = "Question 2 goes here"
        self.fields['q3'].label     = "Question 3 goes here"