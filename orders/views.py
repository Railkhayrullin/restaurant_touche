from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


from .models import CartFood
from .service import get_current_order
from restaurant.models import Food


def add_to_cart(request, *args, **kwargs):
    food_slug = kwargs.get('slug')
    food = Food.objects.get(url=food_slug)
    order = get_current_order(request)
    cart_food = CartFood.objects.get_or_create(order=order, food=food)[0]
    cart_food.quantity += 1
    cart_food.save()
    count = order.order_carts.count()
    return JsonResponse({'count': count})


class CartView(View):
    def get(self, request, *args, **kwargs):
        order = get_current_order(request)
        context = {'order': order}
        return render(request, 'orders/cart.html', context)
