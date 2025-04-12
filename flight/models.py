from django.db import models

# Create your models here.
class flight_register(models.Model):
    date=models.DateField()
    source=models.CharField()
    dest=models.CharField()
    email=models.EmailField()
    
class train_register(models.Model):
    date=models.DateField()
    source=models.CharField()
    dest=models.CharField()
    email=models.EmailField() 

    

