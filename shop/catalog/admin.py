from django.contrib import admin
from .models import Category, Product, Gallery


class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'code', 'slug', 'price',
                    'contents', 'size', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [GalleryInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
