# Generated by Django 4.1.5 on 2023-01-25 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='truckc',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='truckn',
            new_name='pickup',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='truckt',
            new_name='type',
        ),
    ]
