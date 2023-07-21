from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name= "Título")
    description = models.TextField(verbose_name= "Descripción")
    image = models.ImageField(verbose_name= "Imagen", upload_to='projects')
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Fecha de actualización")
    link = models.URLField(verbose_name="Dirección GitHub (código)", null= True, blank=True)

    class Meta:
        verbose_name = 'proyecto'
        #verbose_name = 'proyectos'
        ordering = ["-created"]

    def __str__(self):
        return self.title

