from __future__ import unicode_literals
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone

from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False,default='')
    roll_regex = RegexValidator(regex=r'^(\d{2}|\d{8})([a-z]{2}|[A-Z]{2})\d{2,3}([a-z]{1}|[A-Z]{1})?$', message="Please enter a valid Roll number.")
    rollno = models.CharField(max_length=15, validators=[roll_regex], blank=False, null=False,default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobileno = models.CharField(max_length=16, validators=[phone_regex], blank=False, null=False,default='+91')
    email = models.EmailField(blank=False, null=False,default='')
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__ (self):
        return self.rollno

# Create your models here.
