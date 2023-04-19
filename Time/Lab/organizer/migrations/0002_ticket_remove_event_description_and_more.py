# Generated by Django 4.1.7 on 2023-04-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ticket', models.CharField(max_length=999)),
                ('description_ticket', models.TextField(max_length=100, null=True, verbose_name='')),
                ('price_ticket', models.CharField(max_length=100, null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Билеты',
                'verbose_name_plural': 'Билеты',
            },
        ),
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.AddField(
            model_name='event',
            name='description_event',
            field=models.TextField(max_length=1000, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='age',
            field=models.CharField(choices=[('0+', '0+'), ('6+', '6+'), ('12+', '12+'), ('18+', '18+')], max_length=100, null=True, verbose_name='Возрост'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='event',
            name='price',
            field=models.CharField(max_length=100, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(null=True, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
    ]