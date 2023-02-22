from django.contrib import admin
from .models import Item
from items.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


admin.site.register(Item, ItemAdmin)
