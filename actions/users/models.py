from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from django.core.validators import RegexValidator
import datetime

# Create your models here.


class BranchManager(models.Model):
    """
    The person who manages one branch of the gym
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.ForeignKey("stock.Branch", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.branch})"


class CommonPersonInfo(models.Model):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(default=now)
    dni = models.CharField(
        max_length=8, validators=[RegexValidator(regex="^\d{8}", message="Ingrese un DNI válido")]
    )
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="Other")
    profile_picture = models.ImageField(upload_to="foto_perfil", default="", blank=True, null=True)
    phone = models.BigIntegerField(help_text="Introduzca un número de teléfono válido", default=0)
    address = models.CharField(max_length=30, default="")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} DNI:{self.dni}"


class Trainer(CommonPersonInfo):
    is_active = models.BooleanField(default=True)
    employee_since = models.DateField(auto_now=True)
    employee_until = models.DateField(default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.is_active:
            self.employee_until = datetime.datetime.today()
        super().save(*args, **kwargs)


class MedicalRecord(models.Model):
    height = models.IntegerField(help_text="Ingrese la altura en centímetros")
    weight = models.IntegerField(help_text="Ingrese el peso en kg")
    health_insurance = models.CharField(max_length=30, default="")
    comments = models.TextField(default="")
    emergency_phone = models.BigIntegerField(
        help_text="Introduzca un número de teléfono válido", default=0
    )

    def __str__(self):
        return f"Ficha de {self.client}"


class Client(CommonPersonInfo):
    """
    A client of the gym
    """

    is_active = models.BooleanField(default=True)
    client_since = models.DateField(auto_now=True)
    client_until = models.DateField(default=None, blank=True, null=True)
    routines = models.ManyToManyField(
        "routines.Routine", through="routines.RoutineClient", blank=True
    )
    medical_record = models.OneToOneField(
        MedicalRecord, on_delete=models.CASCADE, null=True, related_name="client"
    )

    def save(self, *args, **kwargs):
        if not self.is_active:
            self.client_until = datetime.datetime.today()
        super().save(*args, **kwargs)


class Score(models.Model):
    """
    The score a Trainer gets from his clients
    """

    score = models.IntegerField(default=0)
    trainer = models.ForeignKey(Trainer, related_name="scores", on_delete=models.CASCADE)
    created = models.DateTimeField(default=now)
