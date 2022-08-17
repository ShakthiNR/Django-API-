from django.db import models

# Create your models here.

class Color(models.Model):
    color_name = models.CharField(max_length=30)

    def __str__(self):
        return self.color_name

class Person(models.Model):
    name= models.CharField(max_length=30)
    age = models.IntegerField()
    dob = models.DateField()
    color = models.ForeignKey(Color,null=True,blank=True,on_delete=models.CASCADE,related_name="color")

    def __str__(self):
        return self.name