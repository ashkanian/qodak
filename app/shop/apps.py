from django.contrib import admin
from shop.models import Item, ItemCategory, Order, OrderItem

admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(Order)
admin.site.register(OrderItem)
