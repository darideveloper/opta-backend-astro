from django.db import models


class TipoLead(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Programa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo_lead = models.ForeignKey(TipoLead, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Momento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    respuesta_momento = models.TextField(null=True, blank=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Submomento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    momento = models.ForeignKey(Momento, on_delete=models.CASCADE)
    programa = models.ForeignKey(
        Programa, null=True, blank=True, on_delete=models.CASCADE)
    tipo_lead = models.ForeignKey(
        TipoLead, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    contenido = models.TextField()
    prioridad = models.IntegerField()
    submomento = models.ForeignKey(Submomento, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenido
    

class Documento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    archivo = models.FileField(upload_to='documentos/')
    palabras_clave = models.TextField()

    def __str__(self):
        return self.nombre