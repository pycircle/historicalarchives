from django.db import models
from django.contrib.auth.models import User

class CommonUser(models.Model):
    """ Common user profile """	
    user = models.OneToOneField(User)
    birth_date = models.DateField()
    GENDER_CHOICES = (
    	('Male', 'M'),
    	('Female', 'F'))
    gender = models.CharField(choices = GENDER_CHOICES, max_length = 6)
