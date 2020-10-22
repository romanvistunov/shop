# Generated by Django 3.1.1 on 2020-09-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.AddField(
            model_name='order',
            name='building_no',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='call_me',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='flat_no',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='fullname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='house_no',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='order',
            name='payonline',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='street',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=10),
        ),
    ]
