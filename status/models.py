from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
    nome = models.CharField(max_length=255)
    peso = models.FloatField()
    altura = models.FloatField()
    usuario = models.OneToOneField(User, on_delete = models.CASCADE)
    
    class Meta:
        db_table = "status"
    def __str__(self):
        return self.nome