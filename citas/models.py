from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone
# Create your models here.
#carlita

opciones_procedimientos = [
        [0, "Endoscopia"],
        [1, "proctoscopia"],
        [2, "Colonoscopia"],
        [3, "EDA+PROCTO"],
        [4, "EDA+COLONO"],

]
opciones_docotores = [
        [0, "Pichilingue"],
        [1, "Cesitar"],
        [2, "Talia"],
        [3, "Carlita"],
        [4, "Ivan"],
]


class procedimientos(models.Model):
    nombre = models.CharField(max_length=50, validators=[RegexValidator(r'^[a-zA-Z\s]+$',
                                                           message='Solo se permiten letras y espacios en los apellidos.')])
    apellidos = models.CharField(max_length=60, validators=[RegexValidator(r'^[a-zA-Z\s]+$',
                                                           message='Solo se permiten letras y espacios en los apellidos.')])

    dni = models.IntegerField(unique=True)
    procedimientos = models.IntegerField(choices=opciones_procedimientos)
    celular = models.IntegerField()
    doctor = models.IntegerField(choices=opciones_docotores)   
    fecha_de_cita = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.nombre
