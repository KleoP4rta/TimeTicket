from django.db import models

##########################################################################################################
class Organization(models.Model):
    name_organizer = models.CharField(null=True, verbose_name='Название организации', max_length=1000)
    email = models.EmailField(null=True)
    number_phone = models.CharField(null=True, max_length=20)
##########################################################################################################
class Event(models.Model):
    title = models.CharField(null=True, verbose_name='Название', max_length=100)
    age = models.IntegerField(null=True, max_length=100, verbose_name='Возраст')
    date_time = models.DateTimeField(null=True)
    price = models.DecimalField(null=True, max_length=100, verbose_name='Цена')
    description_event = models.TextField(null=True, verbose_name='Описание', max_length=1000)
    image = models.ImageField(null=True, verbose_name='Фото', upload_to='media')
    organizer = models.CharField(null=True, verbose_name='Организатор', max_length=500)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'мероприятия'
##########################################################################################################

class Ticket(models.Model):
    name_ticket = models.CharField(max_length=1000, verbose_name='Название')
    description_ticket = models.TextField(null=True, verbose_name='Описание', max_length=100)
    image_ticket = models.ImageField(null=True, verbose_name='Фото')
    price_ticket = models.DecimalField(null=True, max_length=100, verbose_name='Цена')
    
    def __str__(self):
        return self.name_ticket

    class Meta:
        verbose_name = 'Билеты'
        verbose_name_plural = 'Билеты'


