from django.db import models
from apps.products.abstract_models import BaseModel
from django.utils.translation import gettext_lazy as _


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="Category Name")
    slug = models.SlugField(unique=True, verbose_name="Category Slug")
    description = models.TextField(blank=True, verbose_name="Category Description")
    image = models.ImageField(blank=True, upload_to="category/", verbose_name="Category Image")

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=255, unique=True, verbose_name="Tag Name")
    slug = models.SlugField(unique=True, verbose_name="Tag Slug")

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Product Name")
    description = models.TextField(blank=True, verbose_name="Product Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product Price")
    image = models.ImageField(blank=True, upload_to="product/", verbose_name="Product Image")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category", related_name="products")
    tags = models.ManyToManyField(Tag, verbose_name="Tags", related_name="products")

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
