from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import pre_save, post_save, post_delete

class VehicleType(models.Model):
    """Defines vehicle type like sedan, hatchback"""

    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    """Customer information."""

    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    nit_id = models.TextField(blank=True, default="C/F")
    address = models.TextField(blank=True, default="Ciudad")
    phone = PhoneNumberField(blank=True)
   
    def __str__(self):
        return self.name + " " + self.last_name

class Vehicle(models.Model):
   
    reg_id =  models.CharField(max_length=60)  
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    vehicle_type = models.ForeignKey(VehicleType, on_delete = models.PROTECT)
    color = models.CharField(max_length=60)
    description = models.TextField()
    

