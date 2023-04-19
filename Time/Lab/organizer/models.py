from django.db import models


class Event(models.Model):
    title = models.CharField(null=True, verbose_name='Название', max_length=100)
    Age = (
    ('0+', '0+'),
    ('6+', '6+'),
    ('12+', '12+'),
    ('18+', '18+'),
    )
    age = models.CharField(null=True, choices=Age, max_length=100, verbose_name='Возраст')

    date_time = models.DateTimeField(null=True)
    price = models.CharField(null=True, max_length=100, verbose_name='Цена')
    description_event = models.TextField(null=True, verbose_name='', max_length=1000)
    image = models.ImageField(null=True, verbose_name='Фото', upload_to='media')
    organizer = models.CharField(null=True, verbose_name='Организатор', max_length=500)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'мероприятия'


class Ticket(models.Model):
    name_ticket = models.CharField(max_length=1000, verbose_name='Название')
    description_ticket = models.TextField(null=True, verbose_name='', max_length=100)
    image_ticket = models.ImageField(null=True, verbose_name='Фото')
    price_ticket = models.CharField(null=True, max_length=100, verbose_name='Цена')
    
    def __str__(self):
        return self.name_ticket

    class Meta:
        verbose_name = 'Билеты'
        verbose_name_plural = 'Билеты'


