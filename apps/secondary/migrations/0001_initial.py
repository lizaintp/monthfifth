# Generated by Django 5.0.6 on 2024-05-29 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('profession', models.CharField(max_length=255, verbose_name='Профессия')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='Фото сотрудника')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
    ]