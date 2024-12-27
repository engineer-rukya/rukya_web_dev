from django.contrib import admin
from django.contrib.postgres.fields import JSONField
import json
from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)
ensure_ascii=False
encoding='utf-8'

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


