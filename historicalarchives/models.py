from django.db import models

class material(models.Model) #klasa dla materialow
    owner = # wlascicielem jest uzytkownik, 
    title = models.CharField(max_length = 150)
    date = models.
    place = models.CharField(max_length = 150)
    date_of_creation =  models.DateField.auto_now_add #data powstania materialu 
    member_of_collections = #kazdy material moze nalezec do dowolnej ilosci kolekcji


class collection(models.Model) #klasa dla kolekcji
    owner = # wlascicielem jest uzytkownik, albo jest to kolekcja publiczna, wtedy blank - puste pole, ale by default owner == this_user
    founder = # tworca kolekcji musi byc uzytkownikiem, ale nie musi byc tozsamy z wlascicielem
    
