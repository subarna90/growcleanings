# Generated by Django 3.1 on 2021-08-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookzipcode', '0016_auto_20210811_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='price',
            new_name='Commercial_Cleaning_price',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='Domestic_Cleaning_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Residential_Cleaning_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
