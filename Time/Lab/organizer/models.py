from django.db import models


##########################################################################################################
# Организатор
class Organization(models.Model):
    name_organizer = models.CharField(null=True, verbose_name='Название организации', max_length=1000)
    email_organizer = models.EmailField(null=True)
    number_phone_organizer = models.CharField(null=True, max_length=20)

    def __str__(self):
        return self.name_organizer

    class Meta:
        verbose_name = 'Организаторы'
        verbose_name_plural = 'Организаторы'


##########################################################################################################
# Мероприятия
class Event(models.Model):
    title = models.CharField(null=True, verbose_name='Название', max_length=100)
    age = models.IntegerField(null=True, verbose_name='Возраст')
    date_time = models.DateTimeField(null=True, verbose_name='Дата и время')
    buration = models.IntegerField(null=True, verbose_name='Продолжительность', max_length=100)
    price = models.IntegerField(null=True, verbose_name='Цена', max_length=100)
    description_event = models.TextField(null=True, verbose_name='Описание', max_length=1000)
    mini_description_event = models.TextField(null=True, verbose_name='Краткое описание', max_length=100)
    image = models.ImageField(null=True, verbose_name='Фото', upload_to='media')
    organizer = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, verbose_name='Организатор',
                                  max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мероприятия'
        verbose_name_plural = 'мероприятия'


##########################################################################################################
# Участники
class Participants(models.Model):
    name_participants = models.CharField(null=True, verbose_name='ФИО', max_length=100)
    age_participants = models.IntegerField(null=True, verbose_name='Возрост')
    email_participants = models.EmailField(null=True)
    number_phone_participants = models.CharField(null=True, max_length=20)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, verbose_name='Мероприятие')

    def __str__(self):
        return self.name_participants

    class Meta:
        verbose_name = 'Участники'
        verbose_name_plural = 'Участники'


##########################################################################################################
# Билет
class Ticket(models.Model):
    name_ticket = models.CharField(max_length=1000, verbose_name='Название')
    description_ticket = models.TextField(null=True, verbose_name='Описание', max_length=100)
    image_ticket = models.ImageField(null=True, verbose_name='Фото')
    price_ticket = models.IntegerField(null=True, max_length=100, verbose_name='Цена')

    def __str__(self):
        return self.name_ticket

    class Meta:
        verbose_name = 'Билеты'
        verbose_name_plural = 'Билеты'