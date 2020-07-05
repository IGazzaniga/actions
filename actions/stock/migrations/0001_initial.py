# Generated by Django 3.0.8 on 2020-07-05 07:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=30)),
                ("address", models.CharField(default="", max_length=30)),
                ("phone", models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Dealer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(default="", max_length=30)),
                ("last_name", models.CharField(default="", max_length=30)),
                ("email", models.EmailField(default="", max_length=254)),
                (
                    "phone",
                    models.BigIntegerField(
                        default=0, help_text="Introduzca un número de teléfono válido"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=250)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Sell",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=7)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "payment_method",
                    models.CharField(
                        choices=[
                            ("Efectivo", "Efectivo"),
                            ("Tarjeta de crédito", "Tarjeta de crédito"),
                            ("Tarjeta de débito", "Tarjeta de débito"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "card_number",
                    models.BigIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MaxValueValidator(9999999999999999),
                            django.core.validators.MinValueValidator(1111111111111111),
                        ],
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="stock.Item",
                    ),
                ),
                ("image", models.ImageField(default="", upload_to="")),
                ("stock", models.IntegerField(default=0)),
                (
                    "type_of_product",
                    models.CharField(
                        choices=[
                            ("Suplemento", "Suplemento"),
                            ("Máquina", "Máquina"),
                            ("Insumo", "Insumo"),
                            ("Accesorio", "Accesorio"),
                            ("Alimento", "Alimento"),
                            ("Bebida", "Bebida"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
            bases=("stock.item",),
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "item_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="stock.Item",
                    ),
                ),
                ("image", models.ImageField(default="", upload_to="")),
            ],
            bases=("stock.item",),
        ),
        migrations.CreateModel(
            name="SellDetail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField()),
                ("since", models.DateField(blank=True, null=True)),
                ("until", models.DateField(blank=True, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=7)),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stock.Item"
                    ),
                ),
                (
                    "payment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stock.Sell"
                    ),
                ),
            ],
        ),
    ]
