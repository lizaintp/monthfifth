# Generated by Django 5.0.6 on 2024-05-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('desc', models.CharField(max_length=255, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'ЧЗВ',
                'verbose_name_plural': 'ЧЗВ',
            },
        ),
    ]
