# Generated by Django 4.2.2 on 2024-11-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0009_remove_product_images_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="farmer",
            name="is_pending",
            field=models.BooleanField(default=True),
        ),
    ]