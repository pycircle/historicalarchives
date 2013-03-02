from django.db import models
import datetime
from django.contrib.auth.models import User
from tagging.fields import TagField
from django.utils import timezone 
from django import Forms

class Material(models.Model) 
	'''klasa dla materialow'''
	owner = models.ForeignKey(User) # wlascicielem jest uzytkownik, 
	uploader = models.IPAddressField(null = True)#jesli material jest dodawany anonimowo, zapisujemy IP jako tworce 
	title = models.CharField(max_length = 150, unique = True, help_text = '')
	date = models.DateTimeField(blank = True) # DateTimeField jest tymczasowe
	place = models.ForeignKey(Location)
	date_of_creation =  models.DateField.auto_now_add() #data powstania materialu czyli 'teraz' wypelniana automatycznie
	type_of_media = #rodzaj medium: audio, video, plik graficzny, 
	member_of_collections = models.ManyToManyField(Collection)#kazdy material moze nalezec do dowolnej ilosci kolekcji
	description = models.TextField()#opis materialu podany przez uzytkownika
	tags = models.TagField(help_text = '')
	def add_to_collection(self, collection, user):
		if  collection.owner != public and collection.owner != User:
			print "Tylko wlasciciel kolekcji moze dodawac do niej nowe materia³y."
		elif collection.owner == public or collection.owner == User:
			self.member_of_collections.append(collection)
			collection.materials_belonging.append(self)

class UploadMaterial(forms.Form)
	title  = forms.CharField(max_length = 100, help_text = 'Tytul')
	description = forms.TextField(help_text = 'Opis')
	date = forms.?
	place = ?
	file = forms.FileField()
	def save(self):
		new_material = models.Model.material(title = self.cleaned_data['title'],
											description = self.cleaned_data['description']
											date = self.cleaned_data['date']
											place = self.cleand_data['place'])
		return new_material
	
	
	
class Collection(models.Model) 
	'''klasa dla kolekcji'''
	OWNER_CHOICES = ( #uzytkownik wybiera czy chce tworzyc kolekcje wlasna, czy publiczna
		(models.foreignKey(User), 'Ja')
		('', 'Kolekcja publiczna')
	)
	owner =  models.ChoiceField(blank = True, choices = OWNER_CHOICES, default = User)# wlascicielem jest uzytkownik, albo jest to kolekcja publiczna, wtedy blank - puste pole, ale by default owner == this_user
	founder = models.ForeignKey(User) # tworca kolekcji musi byc uzytkownikiem, ale nie musi byc tozsamy z wlascicielem
	title = models.CharField(max_length = 150, unique=True)
	date_of_creation =  models.DateField.auto_now_add() #data powstania materialu czyli 'teraz' wypelniana automatycznie
	materials_belonging = models.ManyToManyField(Material)# materialy ktore naleza do kolekcji
	def make_public(self):
	'''zamienia kolekcje z prywatnej w publiczn¹'''
		self.owner = ''


class request_for_materials(models.Model):
	'''Model dla prosby o udosptepnienie materialow'''
	issuer = models.ForeignKey(User) #osoba ktora publikuje prosbe
	title = models.CharField(max_length = 150, unique = True)
	date_of_creation =  models.DateField.auto_now_add() #data powstania materialu czyli 'teraz' wypelniana automatycznie
	description = models.TextField()#opis prosby o materia³y podany przez uzytkownika



