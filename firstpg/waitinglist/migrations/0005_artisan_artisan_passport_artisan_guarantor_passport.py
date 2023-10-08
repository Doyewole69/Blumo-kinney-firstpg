# Generated by Django 4.2.5 on 2023-10-05 23:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('waitinglist', '0004_remove_artisan_artisan_passport_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artisan',
            name='artisan_passport',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artisan',
            name='guarantor_passport',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
    ]
