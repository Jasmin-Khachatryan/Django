# Generated by Django 4.2.7 on 2023-12-02 08:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_restaurant_data_restaurant_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="restaurant",
            old_name="data",
            new_name="date",
        ),
    ]
