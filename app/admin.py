from django.contrib import admin
from app.models import *
# Register your models here.


admin.site.register(Invoice)
admin.site.register(InvoiceLine)
admin.site.register(Item)
admin.site.register(Customer)