# Generated by Django 4.1.7 on 2023-04-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0005_event_organizer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_organizer', models.CharField(max_length=1000, null=True, verbose_name='Название организации')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('number_phone', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_participants', models.CharField(max_length=100, null=True, verbose_name='')),
                ('age_participants', models.IntegerField(null=True, verbose_name='')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='age',
            field=models.IntegerField(null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description_event',
            field=models.TextField(max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.CharField(max_length=500, null=True, verbose_name='Организатор'),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='description_ticket',
            field=models.TextField(max_length=100, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='price_ticket',
            field=models.IntegerField(max_length=100, null=True, verbose_name='Цена'),
        ),
    ]
