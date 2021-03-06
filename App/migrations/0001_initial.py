# Generated by Django 4.0.3 on 2022-04-01 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('idFamiliar', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fechaDeNacimiento', models.DateField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parentezco',
            fields=[
                ('idParentezco', models.IntegerField(primary_key=True, serialize=False)),
                ('idFamiliar1', models.IntegerField()),
                ('idFamiliar2', models.IntegerField()),
                ('nombreParentezco', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fechaDeInicio', models.DateField(max_length=30)),
            ],
        ),
    ]
