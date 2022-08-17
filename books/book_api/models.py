from turtle import title
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=25)
    author = models.CharField(max_length=35)
    number_of_pages = models.IntegerField()
    quantity = models.IntegerField()
    published_date = models.DateField()

    def __str__(self):
        return self.title