from django.contrib import admin

from .models import Product, Clasification


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'clasification']
    list_filter = ['clasification']
    search_fields = ['name']
    autocomplete_fields = ['clasification']


admin.site.register(Product)
admin.site.register(Clasification)
