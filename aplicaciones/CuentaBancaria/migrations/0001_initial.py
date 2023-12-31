# Generated by Django 4.2.8 on 2023-12-31 15:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cuenta',
            fields=[
                ('id_c', models.AutoField(primary_key=True, serialize=False)),
                ('banco', models.CharField(max_length=20)),
                ('capital', models.FloatField(max_length=6)),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(default='corriente', max_length=10)),
                ('interes', models.FloatField(default=0.0, max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='transaccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('retiro', models.FloatField(max_length=6)),
                ('Abono', models.FloatField(max_length=6)),
                ('fecha', models.DateField(default=datetime.date(2023, 12, 31))),
            ],
        ),
        migrations.CreateModel(
            name='montoefectivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital', models.FloatField(max_length=6)),
                ('id_cta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CuentaBancaria.cuenta')),
            ],
        ),
    ]
