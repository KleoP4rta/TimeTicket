# Generated by Django 4.1.7 on 2023-04-19 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_organization_participants_alter_event_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='buration',
            field=models.IntegerField(max_length=100, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.IntegerField(max_length=100, null=True, verbose_name='Цена'),
        ),
    ]
