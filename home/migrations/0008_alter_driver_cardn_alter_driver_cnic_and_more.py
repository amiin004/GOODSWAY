# Generated by Django 4.1.5 on 2023-01-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_truck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='cardn',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='cnic',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='cvc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='expm',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='expy',
            field=models.IntegerField(),
        ),
    ]