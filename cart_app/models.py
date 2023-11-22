from django.db import models as m


class Product(m.Model):
    desription = m.CharField(max_length=100)
    price = m.IntegerField()
    image = m.CharField(max_length=100)
    discount = m.FloatField(default=1)


class Cart(m.Model):
    product = m.ForeignKey(Product, on_delete=m.CASCADE)
    count = m.IntegerField()
    total = m.DecimalField(decimal_places=2, max_digits=8)

    def calctotal(self):
        return self.count * self.product.price * self.product.discount
