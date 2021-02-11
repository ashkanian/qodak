from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item


class HomeView(ListView):
    model = Item
    template_name = 'home.html'


class ProductView(DetailView):
    model = Item
    template_name = 'product.html'


class CategoryView(ListView):
    model = Item
    template_name = 'category.html'
