# Generated by Django 3.2 on 2021-04-27 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maneger',
            name='cpf',
            field=models.IntegerField(unique=True),
        ),
    ]
