from django.contrib import admin

from base.models import Item, List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass