# Generated by Django 4.2.6 on 2024-01-11 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CuentaBancaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='compra',
            fields=[
                ('id_compra', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(default='No insertada', max_length=25)),
                ('tipo', models.CharField(max_length=20)),
                ('precio_unitario', models.FloatField(max_length=6)),
                ('cantidad', models.FloatField(max_length=0)),
                ('id_transaccion', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CuentaBancaria.transaccion')),
            ],
        ),
    ]
