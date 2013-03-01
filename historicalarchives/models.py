from django.db import models
import datetime
from django.contrib.auth.models import User
from tagging.fields import TagField
from django.utils import timezone 

class Material(models.Model) 
    '''klasa dla materialow'''
    owner = models.ForeignKey(User) # wlascicielem jest uzytkownik, 
    uploader = models.IPAddressField(null = True)#jesli material jest dodawany anonimowo, zapisujemy IP jako tworce 
    title = models.CharField(max_length = 150)
    date = models.DateTimeField(blank = True) # DateTimeField jest tymczasowe
    place = models.ForeignKey(Location)
    date_of_creation =  models.DateField.auto_now_add() #data powstania materialu czyli 'teraz' wypelniana automatycznie
    type_of_media = #rodzaj medium: audio, video, plik graficzny, 
    member_of_collections = models.ManyToManyField(Collection)#kazdy material moze nalezec do dowolnej ilosci kolekcji
    description = models.TextField()#opis materialu podany przez uzytkownika
    tags = models.TagField()
	def add_to_collection(self, collection, user):
		if  collection.owner != public and collection.owner != User:
			print "Tylko wlasciciel kolekcji moze dodawac do niej nowe materia³y."
		elif collection.owner == public or collection.owner == User:
			self.member_of_collections.append(collection)
			collection.materials_belonging.append(self)


class Collection(models.Model) 
    '''klasa dla kolekcji'''
    OWNER_CHOICES = ( #uzytkownik wybiera czy chce tworzyc kolekcje wlasna, czy publiczna
		(models.foreignKey(User), 'Ja')
		('', 'Kolekcja publiczna')
	)
    owner =  models.ForeignKey(blank = True, choices = OWNER_CHOICES, default = User)# wlascicielem jest uzytkownik, albo jest to kolekcja publiczna, wtedy blank - puste pole, ale by default owner == this_user
    founder = models.ForeignKey(User) # tworca kolekcji musi byc uzytkownikiem, ale nie musi byc tozsamy z wlascicielem
    title = models.CharField(max_length = 150)
    date_of_creation =  models.DateField.auto_now_add() #data powstania materialu czyli 'teraz' wypelniana automatycznie
    materials_belonging = models.ManyToManyField(Material)# materialy ktore naleza do kolekcji
    def make_public(self):
    	'''zamienia kolekcje z prywatnej w publiczn¹'''
		self.owner = ''


class request_for_materials(models.Model):
	'''Model dla prosby o udosptepnienie materialow'''
	issuer = models.ForeignKey(User)
	title = models.CharField(max_length = 150)
	date_of_creation =  models.DateField.auto_now_add() #data powstania materialu czyli 'teraz' wypelniana automatycznie
	description = models.TextField()#opis proœby o materia³y podany przez uzytkownika



