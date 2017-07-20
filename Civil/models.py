from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
import os
import string, random
from django.utils import timezone
from homepage.models import Info

# Create your models here.

class Civil(models.Model):
    creator = models.ForeignKey(Info,on_delete=models.CASCADE)
    q1= models.CharField(max_length=50)
    q2= models.TextField()
    q3= models.TextField()
    name = models.CharField(max_length=50, blank=False, null=False,default='')
    is_correct1= models.BooleanField(default=False)
    is_correct2= models.BooleanField(default=False)
    is_correct3= models.BooleanField(default=False)
    score = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(20)],blank=False, null=False,default=0)
    reviewer_1 = models.TextField(blank=False, null=False,default='')
    reviewer_2 = models.TextField(blank=False, null=False,default='')
    reviewer_3 = models.TextField(blank=False, null=False,default='')
    day_to_slot = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],blank=False, null=False,default=0)
    is_selected = models.BooleanField(default = False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__ (self):
        return self.name