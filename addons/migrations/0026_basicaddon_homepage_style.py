# Generated by Django 3.2.18 on 2023-04-24 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addons', '0025_homepagesetup_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicaddon',
            name='homepage_style',
            field=models.CharField(choices=[('carousel ', 'Carousel'), ('static ', 'Static')], default='carousel', max_length=30),
        ),
    ]