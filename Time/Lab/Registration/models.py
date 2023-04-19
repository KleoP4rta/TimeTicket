from django.db import models


class Registration:
    name_user = models.CharField(null=True, max_length=16)
    email = models.EmailField(null=True, max_length=150)
    password1 = models.CharField(null=True, max_length=16)
    password2 = models.CharField(null=True, max_length=16)

    def str(self):
        return self.name_user

    class Meta:
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрация"
