# Generated by Django 4.2.8 on 2024-01-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0002_remove_compra_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='cantid',
            field=models.FloatField(default=0, max_length=6),
        ),
    ]
