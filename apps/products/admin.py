from django.contrib import admin
from apps.products.models import Tag, Category, Product


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)
