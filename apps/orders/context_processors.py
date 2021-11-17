from .cart import Cart


def count_cart(request):
    cart_count = Cart(request).get_total_items()
    if not cart_count:
        cart_count = '0'
    return {'cart_count': cart_count}
