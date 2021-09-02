from django.views.generic import DetailView, CreateView

from .models import Food, Kitchen, Chef
from .forms import ReviewsForm
from orders.service import get_current_order


class ReviewCreateAndFoodView(CreateView):
    """Создание отзыва"""
    form_class = ReviewsForm
    template_name = "restaurant/restaurant.html"
    success_url = '#reviews'

    def get_context_data(self, **kwargs):
        """Функция для вывода списка блюд"""
        kwargs['foods_list'] = Food.objects.filter(in_menu=True)\
                                   .order_by('category')\
                                   .select_related('category', 'kitchen')
        order = get_current_order(self.request)
        kwargs['cart_count'] = order.order_carts.count()
        if not kwargs['cart_count']:
            kwargs['cart_count'] = '0'
        return super(ReviewCreateAndFoodView, self).get_context_data(**kwargs)


class FoodDetailView(DetailView):
    """Полное описание блюда"""
    model = Food
    slug_field = 'url'


class KitchenDetailView(DetailView):
    """Описание кухни мира"""
    model = Kitchen
    slug_field = 'url'


class ChefDetailView(DetailView):
    """Инфо о шеф-поваре"""
    model = Chef
    slug_field = 'url'
