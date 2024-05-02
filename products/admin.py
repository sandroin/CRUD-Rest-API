from django.contrib import admin
from products.models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount']
    list_filter = ['categories']
    search_fields = ['name']
    filter_horizontal = ['categories']


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
