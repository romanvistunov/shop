from django.db import models


class Client(models.Model):
    phone = models.CharField(max_length=20, default="", unique=True)
    fullname = models.CharField(max_length=100, default="")
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100, default="")
    house_no = models.CharField(max_length=10, default="")
    flat_no = models.CharField(max_length=10, default="", blank=True)
    building_no = models.CharField(max_length=10, default="", blank=True)
    postal_code = models.CharField(max_length=10)
    total_orders = models.IntegerField(default=0)

    class Meta:
        ordering = ('-total_orders',)
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return 'Покупатель {}'.format(self.email)
