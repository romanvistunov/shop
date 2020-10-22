from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'fullname', 'email',
                    'city',
                    'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
