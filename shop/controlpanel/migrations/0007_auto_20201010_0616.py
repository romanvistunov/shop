# Generated by Django 3.1.2 on 2020-10-10 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlpanel', '0006_auto_20201010_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
