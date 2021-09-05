from django.db import models

from restaurant.models import Food


class CartFood(models.Model):
    order = models.ForeignKey("Order", verbose_name="заказ", related_name="order_carts", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, verbose_name="блюдо", on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField("количество", default=0)
    price = models.SmallIntegerField("цена", default=0)

    def __str__(self):
        return f"Блюдо: {self.food.name}"

    class Meta:
        verbose_name = "корзина блюд"
        verbose_name_plural = "корзины блюд"

    def get_cost(self):
        return self.quantity * self.price


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
        (BUYING_TYPE_DELIVERY, "Доставка курьером")
    )
    first_name = models.CharField("имя", max_length=255)
    last_name = models.CharField("фамилия", max_length=255)
    phone = models.CharField("телефон", max_length=255)
    email = models.EmailField("email", max_length=255)
    address = models.CharField("адрес", max_length=1024)
    status = models.CharField("статус заказа", max_length=100, choices=STATUS_CHOICES, default=STATUS_NEW)
    buying_type = models.CharField("тип заказа", max_length=100, choices=BUYING_TYPE_CHOICES)
    comment = models.TextField("комментарий к заказу", blank=True, null=True)
    created_at = models.DateTimeField("дата создания заказа", auto_now_add=True)
    updated_at = models.DateTimeField("дата обновления заказа", auto_now=True)
    paid = models.BooleanField("оплачено", default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def get_total_cost(self):
        return sum(cart.get_cost() for cart in self.order_carts.all())
