# Generated by Django 3.1.1 on 2020-09-30 06:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0007_order_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='read_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
