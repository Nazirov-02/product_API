from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['name','price','quantity','discount']

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
  list_display = ['product']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['title']

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['product']