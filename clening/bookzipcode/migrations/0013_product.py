# Generated by Django 3.1 on 2021-08-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookzipcode', '0012_auto_20210811_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('srl_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('price', models.IntegerField(blank=True, max_length=50)),
            ],
        ),
    ]
