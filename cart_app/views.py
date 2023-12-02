from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests


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


@method_decorator(csrf_exempt)  # импортировали модули для csrf_token и создали декоратор
def order_view(request):
    if request.POST:
        # Получение данных от пользователя
        address = request.POST.get('address')
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        items = Cart.objects.all()
        order = ''
        for one in items:
            order += one.product.desription + ' ' + str(one.count) + ' ' + str(one.total) + '\n'
        total = 0
        for i in items:
            total += i.total
        OrderCart.objects.create(address=address, name=name, tel=tel, total=total, order=order)
        items.delete()
        ##########################################################################################
        token = '6311416455:AAGg0yhj3XeD55q7Z3W6uuRqv_isYjeQxJo'
        chat_id = 682235838
        message = order + "Address: " + address + '\nName: ' + name + '\nPhone: ' + tel
        url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}'
        print(requests.get(url).json())
    # return redirect('home')
    #     return HttpResponse('Data successfully')  # Вариант 1
        return JsonResponse({'message': 'Data successfully', 'link': '../'})
    else:
        # Если запрос не POST, то просто отображаем страницу заказа
        return render(request, 'order.html')
