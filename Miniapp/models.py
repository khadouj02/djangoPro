from django.db import models

# Create your models here.



class admin(models.Model):
    idAdmin=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100)
    password=models.CharField(max_length=255)

class Intervenant(models.Model):


    idInter=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom+" "+self.prenom

class Client(models.Model):
    idclient=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    direction=models.CharField(max_length=100)
    def __str__(self):
        return self.nom+" "+self.prenom
    
class Intervention(models.Model):
    idintervention=models.AutoField(primary_key=True)
    date = models.DateField()
    type = models.CharField(max_length=100)
    motive = models.TextField()
    etat = models.CharField(max_length=50)
    id_intervenant = models.ForeignKey('Intervenant', on_delete=models.CASCADE)
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE)
