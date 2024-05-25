from django.contrib import admin
from apps.contacts import models
# Register your models here.

@admin.register(models.Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname')
    