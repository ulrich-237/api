from django.db import models

# Create your models here.

class Book(models.Model):
    titre = models.CharField(max_length=100, null= True)
    auteur = models.CharField(max_length=100, null= True)
    description = models.TextField(max_length=500, null= True)
    prix = models.IntegerField()