# Generated by Django 5.0.6 on 2024-06-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("electronics", "0002_electronics_feature"),
    ]

    operations = [
        migrations.AlterField(
            model_name="electronics",
            name="photo",
            field=models.ImageField(upload_to="photos/"),
        ),
    ]
