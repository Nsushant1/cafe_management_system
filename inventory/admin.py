
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Category, Supplier, InventoryItem
# Register your models here.
@admin.register(InventoryItem)
class InventoryItemAdmin(ImportExportModelAdmin):
    list_display = ('name', 'category', 'quantity', 'unit',)
    search_fields = ("name", "category__name")

admin.site.register(Category)
admin.site.register(Supplier)
