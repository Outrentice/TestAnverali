from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя задачи')
    description = models.TextField(max_length=1440, verbose_name='Описание задачи')
    customer = models.ForeignKey(
        'User', on_delete=models.CASCADE,
        verbose_name='Заказчик', related_name='customer'
    )
    executor = models.ForeignKey(
        'User', on_delete=models.CASCADE,
        null=True, blank=True,
        verbose_name='Исполнитель', related_name='executor'
    )
