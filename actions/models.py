# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from materials.models import Collection, Material

class Action(models.Model):
    '''klasa dla akcji. Na dzien 26 kwietnia 2013, nowe akcje moze uruchamiac tylko admin'''
    title = models.CharField(max_length = 150, unique = True,) # nazwa dla akcji
    slug = models.SlugField(unique=True)
    start_date =  models.DateField(default=datetime.date.today()) # poczatek akcji
    expire_date =  models.DateField() # koniec akcji
    description = models.TextField()#opis akcji  
    aim =  models.TextField(blank = True)#cel akcji, nie musi, ale moze byc wyznaczony 
    participants = models.ManyToManyField(User)#osoby ktore zglosily sie do uczestnictwa w akcji
    linked_collections = models.ManyToManyField(Collection)#kazda akcja moze zostac powiazana z istniejacymi albo wlasnie tworzonymi kolekcjami
    materials_in_response = models.ManyToManyField(Material) # w odpowiedzi na kazda akcje moga powstac jakies materialy
    class Meta:
        ordering = ['-expire_date']
    def __unicode__(self):
        return self.title

    # Create your models here.
