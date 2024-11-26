from django.db import models

class Cliente(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('D', 'Desconocido'),
    ]

    NIVEL_SATISFACCION_CHOICES = [
        (1, 'Muy Insatisfecho'),
        (2, 'Insatisfecho'),
        (3, 'Neutral'),
        (4, 'Satisfecho'),
        (5, 'Muy Satisfecho'),
    ]

    id = models.AutoField(primary_key=True)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default='D')
    saldo = models.FloatField()
    activo = models.BooleanField(default=True)
    nivel_de_satisfaccion = models.IntegerField(choices=NIVEL_SATISFACCION_CHOICES, default=3)

    def __str__(self):
        return f"Cliente {self.id}: {self.genero}, Edad {self.edad}, Saldo {self.saldo}"
