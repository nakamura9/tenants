from django.db import models
from tenant_app.models import CommonFieldsModel

# Create your models here.
class Customer(CommonFieldsModel):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

class Invoice(models.Model):
    date = models.DateField()
    customer = models.ForeignKey('app.customer', on_delete=models.CASCADE)
     
    def __str__(self):
        return f"INV-{self.pk}"
     
class InvoiceLine(models.Model): 
    item = models.ForeignKey('app.item', on_delete=models.CASCADE)
    invoice  = models.ForeignKey('app.invoice', on_delete=models.CASCADE)
    price = models.FloatField() 
    qty = models.FloatField()
    total = models.FloatField()
    
    def __str__(self):
        return f"{self.item}@{self.price} x {self.qty}"
    
class Item(CommonFieldsModel):
    name  = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    
    def __str__(self):
        return self.name