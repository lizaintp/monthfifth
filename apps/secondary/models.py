from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    profession = models.CharField(
        max_length=255,
        verbose_name='Профессия'
    )
    image = models.ImageField(
        verbose_name='Фото сотрудника',
        upload_to='image/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class FAQ(models.Model):
    question = models.CharField(
        max_length=255,
        verbose_name='Вопрос'
    )
    desc = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'ЧЗВ'
        verbose_name_plural = 'ЧЗВ'

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'ЧЗВ'
        verbose_name_plural = 'ЧЗВ'

class Service(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    desc = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='image/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'