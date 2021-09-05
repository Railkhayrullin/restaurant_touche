from django.urls import path

from .views import cart_view, add_to_cart, delete_food, delete_cart, order_create


urlpatterns = [
    path("cart/", cart_view, name="cart"),
    path("add-to-cart/<str:slug>", add_to_cart, name="add_to_cart"),
    path("delete-food/<str:slug>", delete_food, name="delete_food"),
    path("delete-cart/", delete_cart, name="delete_cart"),
    path("create/", order_create, name="order_create"),
]
