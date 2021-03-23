from django.urls import path
from . import views


urlpatterns = [
    path("", views.FoodsView.as_view(), name="home"),
    path("kitchen/<slug:slug>/", views.KitchenDetailView.as_view(), name="kitchen"),
    path("food/<slug:slug>/", views.FoodsDetailView.as_view(), name="food"),
    path("chef/<slug:slug>/", views.ChefsDetailView.as_view(), name="chefs"),
]
