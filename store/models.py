from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Title')
    price = models.DecimalField(max_digits=7, decimal_places=2)


