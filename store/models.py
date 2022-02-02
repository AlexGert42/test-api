from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='Title')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255, default='empty')

    def __str__(self):
        return f'Id: {self.pk} Title: {self.name} Price: {self.price}'

