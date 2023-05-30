from django.contrib import admin

from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', "gender", 'email', 'image']
    search_fields = ['name', 'phone', "gender", 'email', 'image']
    list_filter = ['name', 'phone', "gender", 'email', 'image']

