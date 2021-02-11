from django.urls import path, include
from .views import HomeView, ProductView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>', ProductView.as_view(), name='product'),
]
