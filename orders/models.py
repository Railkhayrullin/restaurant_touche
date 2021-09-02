from django.contrib.sessions.models import Session
from django.db import models
from django.utils import timezone

from restaurant.models import Food
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE)
    phone = models.CharField("номер телефона", max_length=16)
    address = models.CharField("адрес", max_length=255)
    orders = models.ManyToManyField(
        "Order",
        verbose_name="заказы покупателя",
        blank=True,
        related_name="order_customers"
    )

    def __str__(self):
        if self.user.first_name:
            return f"Покупатель: {self.user.first_name}, {self.user.last_name}"
        else:
            return f"Покупатель: {self.user.username}"

    class Meta:
        verbose_name = "покупатель"
        verbose_name_plural = "покупатели"


class CartFood(models.Model):
    order = models.ForeignKey("Order", verbose_name="заказ", related_name="order_carts", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, verbose_name="блюдо", on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField("количество", default=0)
    total_price = models.PositiveIntegerField("общая сумма", default=0)

    def __str__(self):
        return f"Блюдо: {self.food.name}"

    class Meta:
        verbose_name = "корзина блюд"
        verbose_name_plural = "корзины блюд"

    def get_total_price(self):
        return self.quantity * self.food.price


class Order(models.Model):
    STATUS_NEW = "new"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_READY = "is_ready"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"

    BUYING_TYPE_SELF = "self"
    BUYING_TYPE_DELIVERY = "delivery"

    STATUS_CHOICES = (
        (STATUS_NEW, "Новый заказ"),
        (STATUS_IN_PROGRESS, "Заказ в обработке"),
        (STATUS_READY, "Заказ готов"),
        (STATUS_COMPLETED, "Заказ выполнен"),
        (STATUS_CANCELLED, "Заказ отменен"),
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, "Самовывоз"),
        (BUYING_TYPE_DELIVERY, "Доставка")
    )

    customer = models.ForeignKey(
        Customer,
        verbose_name="покупатель",
        related_name="customer_orders",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    session = models.ForeignKey(
        Session,
        verbose_name="сессия",
        related_name='session_orders',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    first_name = models.CharField("имя", max_length=255, blank=True, null=True)
    last_name = models.CharField("фамилия", max_length=255, blank=True, null=True)
    phone = models.CharField("телефон", max_length=255, blank=True, null=True)
    address = models.CharField("адрес", max_length=1024, null=True, blank=True)
    status = models.CharField("статус заказа", max_length=100, choices=STATUS_CHOICES, default=STATUS_NEW)
    buying_type = models.CharField("тип заказа", max_length=100, choices=BUYING_TYPE_CHOICES, default=BUYING_TYPE_SELF)
    comment = models.TextField("комментарий к заказу", blank=True, null=True)
    created_at = models.DateTimeField("дата создания заказа", auto_now=True)
    updated_at = models.DateTimeField("дата обновления заказа", auto_now_add=True)
    final_price = models.IntegerField("финальная сумма", default=0)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def get_total(self):
        total = 0
        for cart in self.order_carts.all():
            total += cart.get_total_price()
        return total
