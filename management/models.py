from django.db import models

class Invoice(models.Model):
    id=models.IntegerField(primary_key=True)
    invoice_number=models.CharField(unique=True,max_length=120)
    customer_name=models.CharField(max_length=120)
    date=models.DateField()

    def __str__(self):
        return f"Invoice {self.invoice_number} for {self.customer_name}"

class Invoice_details(models.Model):
    id=models.IntegerField(primary_key=True)
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE)    
    description=models.CharField(max_length=120)
    quantity=models.PositiveBigIntegerField()
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    line_total=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} - {self.quantity} x {self.unit_price} ({self.line_total})"

#Username:Akbravo
#Password:12345678    
#email address:atharvakumbhar18@gmail.com