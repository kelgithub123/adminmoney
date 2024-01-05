# Generated by Django 4.2.8 on 2024-01-05 03:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CuentaBancaria', '0002_alter_transaccion_fecha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='efectivo',
            name='id_cta',
        ),
        migrations.AddField(
            model_name='efectivo',
            name='id_trans',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='CuentaBancaria.transaccion'),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='fecha',
            field=models.DateField(default=datetime.date(2024, 1, 4)),
        ),
    ]
