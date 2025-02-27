from django.db import models

class cepModel(models.Model):
    cep = models.CharField(max_length=9, null=False, blank=False)
    cidade = models.CharField(max_length=255, null=False, blank=False)
    estado = models.CharField(max_length=255, null=False, blank=False)

    def __str__ (self):
        return f'{self.cep} - {self.cidade}/{self.estado}'
# Create your models here.
