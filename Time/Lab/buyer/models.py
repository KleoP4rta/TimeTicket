from django.db import models


class User(models.Model):
    name_user = models.CharField(null=True, verbose_name='ФИО', max_length=500)
    password_user = models.CharField(null=True, verbose_name='Пароль', max_length=100)
    mail_user = models.CharField(null=True, verbose_name='Почта', max_length=100)

    class_user = models.CharField(null=True, verbose_name='Вид пользователя', max_length=1)

    class_user = models.BooleanField(null=True)

    def __str__(self):
        return self.name_user

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
