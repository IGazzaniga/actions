# Generated by Django 3.0.8 on 2020-07-05 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("stock", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="sell",
            name="branch_manager",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.BranchManager",
            ),
        ),
        migrations.AddField(
            model_name="sell",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.Client"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="branch",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="stock.Branch"
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="dealer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="stock.Dealer"
            ),
        ),
    ]