# Generated by Django 4.1.5 on 2023-01-25 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_truckc_order_destination_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='destination',
            new_name='truckc',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='pickup',
            new_name='truckn',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='type',
            new_name='truckt',
        ),
    ]
