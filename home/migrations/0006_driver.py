# Generated by Django 4.1.5 on 2023-01-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_feedback_home_rename_user_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('cnic', models.IntegerField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('workarea', models.CharField(max_length=30)),
                ('cardn', models.IntegerField(max_length=30)),
                ('cvc', models.IntegerField(max_length=30)),
                ('expm', models.IntegerField(max_length=30)),
                ('expy', models.IntegerField(max_length=30)),
            ],
        ),
    ]
