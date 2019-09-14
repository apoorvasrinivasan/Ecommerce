# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nested_admin
from django.contrib import admin

# Register your models here.
from models import Product, Category, Variant, ProductVariant,ProductType,VariantValues

class VariantInline(admin.TabularInline):
    model = Variant
    pass
# admin.site.register(Variant, VariantAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class VariantValuesInline(nested_admin.NestedStackedInline):
    model = VariantValues
    extra = 2


class ProductVariantInline(nested_admin.NestedTabularInline):
    model = ProductVariant
    inlines = (VariantValuesInline,)
    extra = 1
    pass
# admin.site.register(ProductVariant, ProductVariantAdmin)

class ProductAdmin(nested_admin.NestedModelAdmin):
    inlines = (ProductVariantInline,)
    extra = 1
    pass
admin.site.register(Product, ProductAdmin)

class ProductVariantAdmin(admin.ModelAdmin):
    inlines = (VariantValuesInline,)
    pass
admin.site.register(ProductVariant, ProductVariantAdmin)

class ProductVariantValuesAdmin(admin.ModelAdmin):
    pass
admin.site.register(VariantValues, ProductVariantValuesAdmin)

class ProductTypeAdmin(admin.ModelAdmin):
    inlines = [VariantInline]
    pass
admin.site.register(ProductType, ProductTypeAdmin)
