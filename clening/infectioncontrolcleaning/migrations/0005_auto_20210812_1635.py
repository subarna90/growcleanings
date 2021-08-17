# Generated by Django 3.1 on 2021-08-12 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infectioncontrolcleaning', '0004_time_id_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='time_id',
            name='order',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Order_Ac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept', models.BooleanField(default=False)),
                ('order_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infectioncontrolcleaning.time_id')),
            ],
        ),
    ]
