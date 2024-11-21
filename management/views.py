from django.shortcuts import render
from rest_framework import viewsets
from .serializers import InvoiceSerializer,Invoice_details_Serializer
from .models import Invoice,Invoice_details

# Create your views here.
class InvoiceView(viewsets.ModelViewSet):
    serializer_class=InvoiceSerializer
    queryset=Invoice.objects.all()

class Invoice_details_View(viewsets.ModelViewSet):
    serializer_class=Invoice_details_Serializer
    queryset=Invoice_details.objects.all()    