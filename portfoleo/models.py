
from distutils.command.upload import upload
from email.policy import default
from os import link
from tabnanny import verbose
from tkinter.messagebox import NO
from django.db import models

# Create your models here.
class Project (models.Model):
    title= models.CharField(max_length=201,verbose_name = "Título")
    description = models.TextField( verbose_name = "Descripcion")
    link = models.URLField(verbose_name="Web",null=True, blank=True)
    image= models.ImageField( verbose_name = "Imagen", upload_to="porjects")
    created = models.DateField(auto_now_add = True, verbose_name = "Fecha de creacion")
    update = models.DateField(auto_now = True,verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural ="proyectos"
        ordering=["-created"]

    def __str__(self):
        return self.title    