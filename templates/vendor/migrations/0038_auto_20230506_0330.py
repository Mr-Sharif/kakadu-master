# Generated by Django 3.2.18 on 2023-05-06 02:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0037_alter_coupon_used_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='used_by',
        ),
        migrations.AddField(
            model_name='coupon',
            name='used_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
