# Generated by Django 4.2.8 on 2023-12-31 15:40

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
                ('descripcion', models.CharField(max_length=25)),
                ('tipo', models.CharField(max_length=20)),
                ('precio_unitario', models.FloatField(max_length=6)),
                ('id_cuenta', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CuentaBancaria.cuenta')),
                ('id_efec', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CuentaBancaria.efectivo')),
            ],
        ),
    ]
