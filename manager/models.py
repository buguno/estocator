from django.db import models


class Maneger(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    birthday = models.DateField()
    email = models.CharField(max_length=100)
    cpf = models.CharField(unique=True, max_length=11)

    def __str__(self):
        return self.name
