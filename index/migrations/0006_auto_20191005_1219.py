# Generated by Django 2.2 on 2019-10-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_shedule_ride'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule_ride',
            name='message',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
