# Generated by Django 5.1.7 on 2025-03-13 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='is_main',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
