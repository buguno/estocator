# Generated by Django 3.2 on 2021-04-26 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maneger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
    ]
