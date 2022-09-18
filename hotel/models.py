from django.db import models

# Create your models here.
class Person(models.Model):
     place= models.CharField(max_length=30)
     gest= models.IntegerField()
     arrival=models.DateField()
     leaving = models.DateField()




class Contact(models.Model):
     name_1=models.CharField(max_length=40)
     email=models.EmailField()
     number=models.IntegerField()
     subject=models.CharField(max_length=10)
     textarea=models.CharField(max_length=100)










