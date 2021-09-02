from django.urls import path

from .views import CartView, add_to_cart


urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("add-to-cart/<str:slug>", add_to_cart, name="add_to_cart"),
]
