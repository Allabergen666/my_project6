from django.contrib import admin

from .models import Contact
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'phone', 'image']
    search_fields = ['firstname', 'lastname', 'email', 'phone', 'image']
    list_filter = ['firstname', 'lastname', 'email', 'phone', 'image']

