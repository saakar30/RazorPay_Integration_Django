from django.db import models

# Create your models here.


class Coffee(models.Model):
    name = models.CharField(max_length= 1000 , blank=True)
    amount = models.CharField(max_length=100 , blank=True)
    email = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=1000)
    paid = models.BooleanField(default=False)