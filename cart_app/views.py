from django.shortcuts import render, redirect
from .models import *


def index(request):
    items = Product.objects.all()
    data = {'products': items}
    return render(request, 'index.html', data)


def buy(request, id):
    item = Product.objects.get(id=id)
    if Cart.objects.filter(product_id=id):
        cart_object = Cart.objects.get(product_id=id)
        cart_object.count += 1
        cart_object.total = cart_object.calctotal()
        cart_object.save()
    else:
        Cart.objects.create(count=1, product_id=id, total=item.price)
    return redirect('home')


def cart(request):
    items = Cart.objects.all()
    amount = 0
    for i in items:
        amount += i.total
    data = {'items': items, 'amount': amount}
    return render(request, 'cart.html', data)


def delete(request, id):
    item = Cart.objects.get(id=id)
    item.delete()
    return redirect('cart')
