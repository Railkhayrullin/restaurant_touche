from django.views.generic import DetailView, CreateView

from .models import Food, Kitchen, Chef
from .forms import ReviewsForm


class FoodCreateView(CreateView):
    """Создание отзыва"""
    form_class = ReviewsForm
    template_name = "restaurant/restaurant.html"
    success_url = '#reviews'

    def get_context_data(self, **kwargs):
        """Функция для вывода списка блюд"""
        kwargs['foods_list'] = Food.objects.filter(in_menu=True)\
                                   .order_by('category')\
                                   .select_related('category', 'kitchen')

        return super(FoodCreateView, self).get_context_data(**kwargs)


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
