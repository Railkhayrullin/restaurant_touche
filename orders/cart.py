from django.conf import settings
from .models import Food


class Cart(object):
    def __init__(self, request):
        """Инициализируем корзину"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """Перебор элементов в корзине и получение продуктов из базы данных"""
        product_ids = self.cart.keys()

        # получение объектов product и добавление их в корзину
        products = Food.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item

    def add(self, product, quantity=1, update_quantity=False):
        """Добавить продукт в корзину или обновить его количество"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart

        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def get_total_items(self):
        """Подсчет количества товаров в корзине"""
        count = 0
        for item in self.cart.values():
            count += 1
        return count

    def get_total_price(self):
        """Подсчет стоимости товаров в корзине"""
        return sum(int(item['price']) * int(item['quantity']) for item in self.cart.values())

    def remove(self, product):
        """Удаление товара из корзины"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """Удаление корзины из сессии"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
