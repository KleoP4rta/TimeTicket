# Generated by Django 4.2 on 2023-04-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0004_remove_event_date_remove_event_time_event_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.CharField(max_length=500, null=True, verbose_name='Оргонизатор'),
        ),
    ]
