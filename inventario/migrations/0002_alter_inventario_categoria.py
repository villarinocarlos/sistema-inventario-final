# Generated by Django 5.0.7 on 2024-08-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='categoria',
            field=models.CharField(blank=True, choices=[('electronica', 'Electrónica'), ('hogar', 'Hogar'), ('entretenimiento', 'Entretenimiento')], max_length=100, null=True),
        ),
    ]
