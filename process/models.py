from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class TipoLead(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Programa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_lead = models.ForeignKey(TipoLead, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.tipo_lead}"
    
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'


class Momento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.programa}"
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class Submomento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    momento = models.ForeignKey(Momento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.momento}"
    
    class Meta:
        verbose_name = 'Subitem'
        verbose_name_plural = 'Subitems'


class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, default='', blank=True)
    contenido = models.TextField()
    image = models.ImageField(upload_to='respuestas/', null=True, blank=True)
    prioridad = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    submomento = models.ForeignKey(Submomento, on_delete=models.CASCADE)
    documento = models.ForeignKey(
        'Documento',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.titulo} - {self.submomento}"
    
    @property
    def titulo_clean(self):
        return self.titulo if self.titulo else "Sin Título"
    
    @property
    def submomento_str(self):
        return f'Respuesta al submomento: "{self.submomento.nombre}"'
    
    titulo_clean.fget.short_description = 'Título'
    submomento_str.fget.short_description = 'Submomento'
    
    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
    

class Documento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='documentos/')
    palabras_clave = models.TextField(
        help_text='Palabras clave separadas por coma'
    )

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'