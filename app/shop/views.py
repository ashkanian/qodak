from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, Order, OrderItem


class HomeView(ListView):
    model = Item
    template_name = 'index.html'


class ProductView(DetailView):
    model = Item
    template_name = 'product.html'


class CategoryView(ListView):
    model = Item
    template_name = 'category.html'


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = oreder_qs[0]
        #Checking for items in order and quantity checking
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order-item.save()

