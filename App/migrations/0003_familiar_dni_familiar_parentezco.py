# Generated by Django 4.0.3 on 2022-04-05 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_delete_parentezco'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='dni',
            field=models.IntegerField(default=9999999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='familiar',
            name='parentezco',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
