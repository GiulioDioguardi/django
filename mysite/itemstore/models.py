from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    stock = models.IntegerField('number in stock')
    description = models.TextField()

    def __str__(self):
        return self.name

    def is_out_of_stock(self):
        return self.stock <= 0

    is_out_of_stock.boolean = True
    is_out_of_stock.short_description = 'Out of stock?'
