# Generated by Django 4.2.5 on 2023-10-04 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waitinglist', '0003_artisan_guarantor_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artisan',
            name='artisan_passport',
        ),
        migrations.RemoveField(
            model_name='artisan',
            name='guarantor_passport',
        ),
    ]
