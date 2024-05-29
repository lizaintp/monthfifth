from django.contrib import admin

from apps.secondary import models
# Register your models here.

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')