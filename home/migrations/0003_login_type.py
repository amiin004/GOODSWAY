# Generated by Django 4.1.5 on 2023-01-22 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='type',
            field=models.TextField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
