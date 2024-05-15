from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    experience = models.CharField(max_length=1440, blank=True, null=True, verbose_name='Опыт(Описание)')
    role = models.CharField(max_length=255, null=False, verbose_name='Роль')

    def __str__(self):
        return f"{self.username} - {self.role}"
