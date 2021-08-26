from django.db import models
from django.utils import timezone

from restaurant.models import Food
from django.contrib.auth import get_user_model

User = get_user_model()


class CartFood(models.Model):
    user = models.ForeignKey("Customer", verbose_name="покупатель", on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", verbose_name="корзина", related_name="cart_foods", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, verbose_name="блюдо", on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField("количество", default=1)
    total_price = models.PositiveIntegerField("общая сумма")

    def __str__(self):
        return f"Блюдо: {self.food.name} (для корзины)"


class Cart(models.Model):
    owner = models.ForeignKey("Customer", verbose_name="покупатель", on_delete=models.CASCADE)
    foods = models.ManyToManyField(CartFood, blank=True, related_name="foods_cart")
    total_foods = models.PositiveSmallIntegerField(default=0)
    final_price = models.PositiveIntegerField("финальная сумма")
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE)
    phone = models.CharField("номер телефона", max_length=16)
    address = models.CharField("адрес", max_length=255)

    def __str__(self):
        return f"Покупатель: {self.user.first_name}, {self.user.last_name}"


class Order(models.Model):
    STATUS_NEW = "new"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_READY = "is_ready"
    STATUS_COMPLETED = "completed"

    BUYING_TYPE_SELF = "self"
    BUYING_TYPE_DELIVERY = "delivery"

    STATUS_CHOICES = (
        (STATUS_NEW, "Новый заказ"),
        (STATUS_IN_PROGRESS, "Заказ в обработке"),
        (STATUS_READY, "Заказ готов"),
        (STATUS_COMPLETED, "Заказ выполнен"),
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, "Самовывоз"),
        (BUYING_TYPE_DELIVERY, "Доставка")
    )

    customer = models.ForeignKey(Customer, verbose_name="покупатель", on_delete=models.CASCADE)
    first_name = models.CharField("имя", max_length=255)
    last_name = models.CharField("фамилия", max_length=255)
    phone = models.CharField("телефон", max_length=255)
    address = models.CharField("адрес", max_length=1024, null=True, blank=True)
    status = models.CharField("статус заказа", max_length=100, choices=STATUS_CHOICES, default=STATUS_NEW)
    buying_type = models.CharField("тип заказа", max_length=100, choices=BUYING_TYPE_CHOICES, default=BUYING_TYPE_SELF)
    comment = models.TextField("комментарий к заказу", null=True, blank=True)
    order_date = models.DateField("дата получения заказа", default=timezone.now)
