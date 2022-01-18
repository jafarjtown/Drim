from os import name
from django.db import models

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=100)
    shops = models.ManyToManyField('Shop', blank=True, related_name='markets')
    def __str__(self) -> str:
        return self.name
class Shop(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField('Item', blank=True, related_name='shop')

    def __str__(self) -> str:
        return self.name
class Item(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    item = models.FileField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name

    def get_price(self):
        if self.price <= 0:
            return f'FREE'
        return self.price
class Cart(models.Model):
    user = models.OneToOneField('accounts.User', related_name='cart', on_delete=models.CASCADE)
    items = models.ManyToManyField('ItemCart', blank=True)

    def price(self, it):
        if self.items.filter(item__id = it).exists():
            item = self.items.get(item__id = it)
            return item.price()
        return 0

class ItemCart(models.Model):
    item = models.ForeignKey("Item",  on_delete=models.CASCADE)
    amount = models.IntegerField()

    def price(self):
        return self.item.price * self.amount
    