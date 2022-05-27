from django.db import models
from datetime import datetime

# Create your models here.

class Machine(models.Model):
    
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('MAc - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
)

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=6)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')

class Server(models.Model):
    id = models.AutoField(
                    primary_key = True,
                    editable = False)
    nom = models.CharField(max_length= 6)
    
    def __str__(self):
        return str(self.id) + " --> " + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom

class Personnel(models.Model):
    id_secu = models.IntegerField(
                    primary_key = True,
                    editable = True,
                    max_length=13)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id) + " --> " + self.nom
    
    def get_name(self):
        return str(self.id) + " " + self.nom
