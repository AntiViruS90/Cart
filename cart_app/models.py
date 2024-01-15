from django.db import models as m
from django.contrib.auth.models import User


class Product(m.Model):
    desription = m.CharField(max_length=100)
    price = m.IntegerField()
    image = m.CharField(max_length=100)
    discount = m.FloatField(default=1)

    def __str__(self):
        return self.desription


class Cart(m.Model):
    user = m.ForeignKey(User, on_delete=m.CASCADE, null=True, blank=True)
    product = m.ForeignKey(Product, on_delete=m.CASCADE)
    count = m.IntegerField()
    total = m.DecimalField(decimal_places=2, max_digits=8)

    def calctotal(self):
        return self.count * self.product.price * self.product.discount


class OrderCart(m.Model):
    address = m.CharField(max_length=100)
    name = m.CharField(max_length=50)
    tel = m.CharField(max_length=20)
    total = m.IntegerField()
    order = m.TextField()

