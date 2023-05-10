# Generated by Django 4.2.1 on 2023-05-10 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=256)),
                ('nombre', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=32)),
                ('fecha_nac', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Clases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=164)),
                ('dia', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=256)),
                ('nombre', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=32)),
                ('fecha_nac', models.DateField()),
            ],
        ),
    ]