from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True, null=True, editable=False ) #con blank=True podemos guardar dejando campos vacios
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)#con null=True el campo no siempre trae un valor
    anulate = models.BooleanField('Anulado', default=False)#con unique=true nos aseguramos que ese campo es unico en toda la tabla

    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la Empresa'
        ordering = ['-name']
        unique_together = ('name', 'shor_name')

    def __str__(self):
        return str(self.id)+' - '+self.name+' - '+self.shor_name