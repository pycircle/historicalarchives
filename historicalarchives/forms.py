from django import forms
import datetime

class UploadMaterial(forms.Form)
	title  = forms.CharField(max_length = 100, help_text = 'Tytul')
	description = forms.TextField(help_text = 'Opis')
	date = forms.DateField(initial=datetime.date.today)
    #do zastnowienia place = 
	file = forms.FileField()
