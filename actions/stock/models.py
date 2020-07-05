from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class Branch(models.Model):
    """
    A branch of the gym
    """

    name = models.CharField(max_length=30, default="")
    address = models.CharField(max_length=30, default="")
    phone = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.address}"


class Dealer(models.Model):
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    email = models.EmailField(max_length=254, default="")
    phone = models.BigIntegerField(
        help_text="Introduzca un número de teléfono válido", default=0
    )

    def __str__(self):
        return f"{self.name} {self.address}"


class Item(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(Item):
    image = models.ImageField(default="")
    stock = models.IntegerField(default=0)
    TYPES = (
        ("Suplemento", "Suplemento"),
        ("Máquina", "Máquina"),
        ("Insumo", "Insumo"),
        ("Accesorio", "Accesorio"),
        ("Alimento", "Alimento"),
        ("Bebida", "Bebida"),
    )
    type_of_product = models.CharField(max_length=30, choices=TYPES)
    dealer = models.ForeignKey(Dealer, on_delete=models.PROTECT)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Service(Item):
    image = models.ImageField(default="")


class Sell(models.Model):
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    PAYMENT_METHOD = (
        ("Efectivo", "Efectivo"),
        ("Tarjeta de crédito", "Tarjeta de crédito"),
        ("Tarjeta de débito", "Tarjeta de débito"),
    )
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHOD)
    branch_manager = models.ForeignKey(
        "users.BranchManager", on_delete=models.CASCADE, null=True
    )
    card_number = models.BigIntegerField(
        null=True,
        blank=True,
        validators=[
            MaxValueValidator(9999999999999999),
            MinValueValidator(1111111111111111),
        ],
    )
    client = models.ForeignKey("users.Client", on_delete=models.CASCADE)


class SellDetail(models.Model):
    quantity = models.IntegerField()
    since = models.DateField(null=True, blank=True)
    until = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    payment = models.ForeignKey(Sell, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
