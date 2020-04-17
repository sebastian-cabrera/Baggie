# Generated by Django 2.2.6 on 2020-04-14 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empaque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=15)),
                ('Proveedor', models.CharField(max_length=25)),
                ('Modelo', models.CharField(max_length=30)),
                ('Dimensiones', models.CharField(max_length=15)),
                ('Peso_Max', models.IntegerField(default=0)),
                ('Cantidad_Usos', models.IntegerField(default=0)),
            ],
        ),
    ]