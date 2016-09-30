from django.db import models


# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    

class Cat(models.Model):
    name = models.CharField(max_length = 200)
    date_of_bright = models.DateField(blank = True, null = True)
    male = models.BooleanField(default=True)
    breed = models.ForeignKey(Breed)
    image = models.ImageField(null=True, blank=True)
    
        

    def __str__(self):
        return self.name