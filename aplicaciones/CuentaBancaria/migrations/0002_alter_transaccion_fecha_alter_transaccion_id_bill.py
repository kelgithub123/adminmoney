# Generated by Django 4.2.8 on 2024-01-05 22:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CuentaBancaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 16, 50, 27, 134853)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='id_bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CuentaBancaria.billetera'),
        ),
    ]