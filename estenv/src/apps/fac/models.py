from django.db import models

from ..vehicle.models import Vehicle


class Invoice(models.Model):
    """Model definition for Invoice."""



    
    factura_number = models.CharField(max_length=12)
    date = models.DateTimeField(auto_now_add=True)
    end_hour = models.TimeField()
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.order.id)
    
class InvoiceDetail(models.Model):
   
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    start_hour = models.TimeField()
