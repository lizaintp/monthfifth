from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Contacts(models.Model):
    locate = models.CharField(
        max_length=255,
        verbose_name='Локация'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        verbose_name='Почта',
    )
    def __str__(self):
        return self.locate
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

