# Generated by Django 3.1.1 on 2020-09-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_remove_order_read_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
