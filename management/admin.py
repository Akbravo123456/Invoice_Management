from django.contrib import admin
from .models import Invoice,Invoice_details

class InvoiceAdmin(admin.ModelAdmin):
    list_display=('id','invoice_number','customer_name','date')
admin.site.register(Invoice,InvoiceAdmin)  

class Invoice_details_Admin(admin.ModelAdmin):
    list_display=('id','invoice','description','quantity','unit_price','line_total')
admin.site.register(Invoice_details,Invoice_details_Admin) 

