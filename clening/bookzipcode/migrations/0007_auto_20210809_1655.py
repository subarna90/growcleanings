# Generated by Django 3.1 on 2021-08-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookzipcode', '0006_auto_20210809_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookorder',
            name='total_price',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]