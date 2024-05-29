# Generated by Django 5.0.6 on 2024-05-29 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='image',
        ),
        migrations.AddField(
            model_name='contacts',
            name='email',
            field=models.EmailField(default=1, max_length=254, verbose_name='Почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacts',
            name='locate',
            field=models.CharField(default=1, max_length=255, verbose_name='Локация'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacts',
            name='phone',
            field=models.CharField(default=1, max_length=255, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
    ]
