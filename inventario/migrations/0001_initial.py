# Generated by Django 5.0.7 on 2024-08-04 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('categoria', models.CharField(blank=True, max_length=100, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=19)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
