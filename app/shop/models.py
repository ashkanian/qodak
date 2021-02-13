from django.db import models
from django.conf import settings
from django.shortcuts import reverse

LABEL_CHOICES = (
    ('N', 'danger'),
    ('B', 'primary'),
)


class ItemCategory(models.Model):
    title = models.CharField(max_length=155)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class ItemBrand(models.Model):
    title = models.CharField(max_length=155, unique=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=155)
    short_desc = models.TextField(null=True)
    long_desc = models.TextField(null=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(
        ItemCategory, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(
        ItemBrand, on_delete=models.CASCADE, null=True, blank=True)
    label = models.CharField(choices=LABEL_CHOICES,
                             max_length=1, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.item.title} = {self.quantity}'


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user
