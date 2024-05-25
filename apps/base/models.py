from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Settings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название сайта',
        blank=False,
        null=False,
    )
    desc = RichTextField(
        verbose_name='Описание сайта'
    )
    logo = models.ImageField(
        verbose_name='Логотип сайта',
        upload_to='logo/',
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    phone = models.PositiveIntegerField(
        verbose_name='Номер телефона'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'

