import pytz
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    phone_regex = RegexValidator(
        regex=r'^7\d{10}$',
        message='Номер телефона клиента в формате 7XXXXXXXXXX'
    )
    phone_number = models.CharField(
        max_length=11,
        validators=[phone_regex],
        verbose_name='Номер телефона',
        unique=True,
    )
    mobile_operator_code = models.CharField(
        max_length=3,
        verbose_name='Код мобильного оператора',
        editable=False
    )
    tag = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Поиск тегов'
    )
    timezone = models.CharField(
        max_length=32,
        choices=TIMEZONES,
        verbose_name='Часовой пояс',
        default='UTC'
    )

    def save(self, *args, **kwargs):
        self.mobile_operator_code = str(self.phone_number)[1:4]
        return super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return f'Клиент {self.id} с номером {self.phone_number}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    date_start = models.DateTimeField(
        verbose_name='Дата начала рассылки'
    )
    date_end = models.DateTimeField(
        verbose_name='Дата окончания рассылки'
    )
    time_start = models.TimeField(
        verbose_name='Время начала отправки сообщения'
    )
    time_end = models.TimeField(
        verbose_name='Время окончания отправки сообщения'
    )
    text = models.TextField(
        max_length=255,
        verbose_name='Текст сообщения'
    )
    mobile_operator_code = models.CharField(
        max_length=3,
        blank=True,
        verbose_name='Поиск по коду мобильного оператора'
    )
    tag = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Поиск по тегам'
    )

    @property
    def to_send(self):
        now = timezone.now()
        if self.date_start <= now <= self.date_end:
            return True
        return False

    def __str__(self):
        return f'Рассылка {self.id} от {self.date_start}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    SENT = 'отправлено'
    NO_SENT = 'не отправлено'

    STATUS_CHOICES = [
        (SENT, 'Отправлено'),
        (NO_SENT, 'Не отправлено'),
    ]
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания'
    )
    sending_status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        verbose_name='Статус отправки'
    )
    mailing = models.ForeignKey(
        Mailing,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Рассылка'
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name='Клиент'
    )

    def __str__(self):
        return (f'Сообщение {self.id} с текстом {self.mailing} '
                f'для {self.client}')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
