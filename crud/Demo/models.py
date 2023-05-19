from django.db import models

# Create your models here.

class empleado(models.Model):
    Nombres = models.CharField( max_length=50)
    Apellidos = models.CharField(max_length=50)
    Tipo_de_Documento = models.CharField(max_length=50)
    Fecha_de_Nacimiento = models.CharField(max_length=50)
    Fecha_de_Vinculacion_a_la_compañia = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    Salario = models.IntegerField()
    Tiempo_de_Vinculacion_a_la_compañia = models.CharField(max_length=50)
    Edad_actual_del_empleado = models.IntegerField()
    creado_en = models.DateTimeField(auto_created=True)


    def __str__(self) -> str:
        return self.Nombres
