# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Market, Shop, Item


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'page')
    list_filter = ('page',)
    raw_id_fields = ('shops',)
    search_fields = ('name',)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    raw_id_fields = ('items',)
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'item', 'price')
    search_fields = ('name',)