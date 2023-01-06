from django.db import models
from django.utils import timezone 

# Create your models here.
def apres_deux_semaines():
    return timezone.now() + timezone.timedelta(days=14)
    
class Livre(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=32)

class Lecteur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length = 20)
    prenom = models.CharField(max_length=24)
    num_phone = models.CharField(max_length = 12, unique = True)

class Retrait(models.Model):
    id = models.AutoField(primary_key=True)
    date_retrait = models.DateTimeField(auto_now_add=True)

class Remise(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=apres_deux_semaines)


    
   


