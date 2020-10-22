from django.db import models
from catalog.models import Product
from controlpanel.models import Client


class Order(models.Model):
    phone = models.CharField(max_length=20, default="")
    fullname = models.CharField(max_length=100, default="")
    email = models.EmailField()
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100, default="")
    house_no = models.CharField(max_length=10, default="")
    flat_no = models.CharField(max_length=10, default="", blank=True)
    building_no = models.CharField(max_length=10, default="", blank=True)
    postal_code = models.CharField(max_length=10)
    comment = models.TextField(max_length=550, default="", blank=True)
    call_me = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    client_exists = models.BooleanField(default=False)
    client = models.ForeignKey(
        Client, related_name='client', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
