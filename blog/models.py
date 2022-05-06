from distutils.text_file import TextFile
from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=150)
    qty = models.IntegerField()
    price = models.IntegerField()
    DisplayFields = ['id', 'name', 'qty', 'price', 'total']

    def total(self):
        total = self.qty * self.price
        return total
