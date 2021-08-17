# Generated by Django 3.1 on 2021-08-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookzipcode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('srl', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('postcode', models.CharField(max_length=10)),
                ('service_details', models.CharField(max_length=100)),
                ('infection', models.CharField(max_length=100)),
                ('total_price', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Chdomestic',
        ),
    ]
