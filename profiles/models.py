from django.db import models

class User(models.Model):
  """ Common user profile """
	
    login = models.CharField(max_length = 25, unique = True)
    #password = 
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 45)
    birth_date = models.DateField()
    GENDER_CHOICES = (
    	('Male', 'M'),
    	('Female', 'F'))
    gender = models.CharField(choices = GENDER_CHOICES)
    mail =	models.EmailField(max_length = 75, unique = True)
