from django.contrib import admin
from .models import *


@admin.register(PersonModel)
class PersonModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'address']
    list_display_links = ['first_name']

    
