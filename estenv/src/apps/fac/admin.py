from django.contrib import admin
from .models import Invoice,InvoiceDetail
from django.utils.safestring import mark_safe

admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
