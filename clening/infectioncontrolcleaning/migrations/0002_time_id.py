# Generated by Django 3.1 on 2021-08-12 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infectioncontrolcleaning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(blank=True, null=True)),
                ('day_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='infectioncontrolcleaning.post')),
            ],
        ),
    ]