from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Contacts(models.Model):
    fullname = models.CharField(
        max_length=255,
        verbose_name='ФИО',
        blank=False,
        null=False,
    )
    desc = RichTextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        verbose_name='Логотип сайта',
        upload_to='logo/',
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолии'

