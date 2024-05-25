from django.contrib import admin
from apps.base import models
# Register your models here.

@admin.register(models.Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'email', 'phone')
    