from backend.admin import admin_site
from django.contrib import admin

from .forms import ProductForm
from .models import SubCategory,Category,Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    form=ProductForm
admin_site.register(SubCategory)
admin_site.register(Category)
admin_site.register(Product,ProductAdmin)