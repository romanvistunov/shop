# Generated by Django 3.1.2 on 2020-10-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controlpanel', '0002_delete_userreadorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(default='', max_length=20)),
                ('fullname', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(default='', max_length=100)),
                ('house_no', models.CharField(default='', max_length=10)),
                ('flat_no', models.CharField(blank=True, default='', max_length=10)),
                ('building_no', models.CharField(blank=True, default='', max_length=10)),
                ('postal_code', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Покупатель',
                'verbose_name_plural': 'Покупатели',
                'ordering': ('-id',),
            },
        ),
    ]
