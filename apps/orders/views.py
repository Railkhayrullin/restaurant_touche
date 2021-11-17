from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from apps.restaurant.models import Food
from .models import CartFood
from .cart import Cart
from .forms import OrderCreateForm
from .service import send_messages_to_managers


def add_to_cart(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Food, url=slug)
    cart.add(product=product)
    count = cart.get_total_items()
    return JsonResponse({'count': count})


def delete_food(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Food, url=slug)
    cart.remove(product)
    return redirect('cart')


def delete_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('home')


def cart_view(request):
    cart = Cart(request)
    return render(request, 'orders/cart.html', {'cart': cart})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()

            obj_list = [
                CartFood(order=order,
                         food=item['product'],
                         quantity=item['quantity'],
                         price=item['price'])
                for item in cart
            ]

            # создание объектов БД одним запросом
            CartFood.objects.bulk_create(obj_list)

            # отправка писем о новом заказе менеджерам
            send_messages_to_managers(order)

            # очистка корзины
            cart.clear()
            return render(request, 'orders/order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order_create.html',
                  {'cart': cart, 'form': form})
