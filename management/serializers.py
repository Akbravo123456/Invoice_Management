from rest_framework import serializers
from .models import Invoice,Invoice_details

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields=('id','invoice_number','customer_name','date')

class Invoice_details_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice_details
        fields=('id','invoice','description','quantity','unit_price','line_total')    