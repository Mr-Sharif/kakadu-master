# Generated by Django 3.2.18 on 2023-06-05 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0044_auto_20230604_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='flatrate_amount',
        ),
    ]