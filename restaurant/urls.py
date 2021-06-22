from django.urls import path
from .views import FoodCreateView, KitchenDetailView, FoodDetailView, ChefDetailView


urlpatterns = [
    path("", FoodCreateView.as_view(), name="home"),
    path("kitchen/<slug:slug>/", KitchenDetailView.as_view(), name="kitchen"),
    path("food/<slug:slug>/", FoodDetailView.as_view(), name="food"),
    path("chef/<slug:slug>/", ChefDetailView.as_view(), name="chefs"),
]
