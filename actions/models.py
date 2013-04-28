# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class Actions(models.Model):
    '''klasa dla akcji. Na dzien 26 kwietnia 2013, nowe akcje moze uruchamiac tylko admin'''
	title = models.CharField(max_length = 150, unique = True,) # nazwa dla akcji
	start_date =  models.DateField(default=datetime.date.today()) # poczatek akcji
	expire_date =  models.DateField() # koniec akcji
	description = models.TextField()#opis akcji  
	aim =  models.TextField(blank = True)#cel akcji, nie musi, ale moze byc wyznaczony 
	participants = models.ManyToManyField(User)#osoby ktore zglosily sie do uczestnictwa w akcji
	linked_collections = models.ManyToManyField(Collection)#kazda akcja moze zostac powiazana z istniejacymi albo wlasnie tworzonymi kolekcjami
	materials_in_response = models.ManyToManyField(Material) # w odpowiedzi na kazda akcje moga powstac jakies materialy
	def __str__(self):
		return self.name

	# Create your models here.
