from django.db import models

# Переменная для нулевых полей
NULLABLE = {'blank': True, 'null': True}


class Template(models.Model):
    """Модель шаблона, которая получает только названия полей пользователя
    обязательное значение только имя,
    остальное пользователь может установить по своему желанию"""
    name = models.CharField(
        max_length=128, verbose_name="Название шаблона")
    date = models.CharField(
        max_length=128, verbose_name="Дата", **NULLABLE)
    telephone = models.CharField(
        max_length=128, verbose_name="Телефон", **NULLABLE)
    email = models.CharField(
        max_length=128, verbose_name="Электронная почта", **NULLABLE)
    text = models.CharField(
        max_length=128, verbose_name="Текст", **NULLABLE)
