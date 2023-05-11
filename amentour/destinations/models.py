from django.db import models

# Create your models here.
class Destination(models.Model):

    name =models.CharField(max_length=100)
    discription =models.TextField()
    hotel = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    
class Package(models.Model):
    name =models.CharField(max_length=100)
    discription =models.TextField()
    hotel = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    duration = models.CharField(max_length=10)
    people_number=models.PositiveIntegerField()
    image = models.ImageField(upload_to='media')
    def __str__(self):
        return self.name