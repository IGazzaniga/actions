from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

# Create your models here.


class BranchManager(models.Model):
    """
    The person who manages one branch of the gym
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey("users.Branch", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to="foto_perfil", default="")
    phone = models.BigIntegerField(
        help_text="Introduzca un número de teléfono válido", default=0
    )
    address = models.CharField(max_length=30, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Score(models.Model):
    """
    The score a Trainer gets from his clients
    """

    score = models.IntegerField(default=0)
    trainer = models.ForeignKey(
        Trainer, related_name="scores", on_delete=models.CASCADE
    )
    created = models.DateTimeField(default=now)


class Client(models.Model):
    """
    A client of the gym
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(default=now)
    dni = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to="foto_perfil", default="")
    phone = models.BigIntegerField(
        help_text="Introduzca un número de teléfono válido", default=0
    )
    address = models.CharField(max_length=30, default="")
    trainer = models.ForeignKey(Trainer, on_delete=models.PROTECT)
    routines = models.ManyToManyField(
        "routines.Routine", through="routines.RoutineClient", blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MedicalRecord(models.Model):
    height = models.IntegerField(help_text="Ingrese la altura en centímetros")
    weight = models.IntegerField(help_text="Ingrese el peso en kg")
    GENDER_CHOICES = (
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino"),
    )
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    health_insurance = models.CharField(max_length=30, default="")
    comments = models.TextField(default="")
    emergency_phone = models.BigIntegerField(
        help_text="Introduzca un número de teléfono válido", default=0
    )
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
