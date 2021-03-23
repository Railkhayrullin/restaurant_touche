from django.views.generic import DetailView, CreateView
from .models import Foods, Kitchen, Chefs
from .forms import ReviewsForm


class FoodsView(CreateView):
    """Список блюд"""
    form_class = ReviewsForm
    template_name = "restaurant/restaurant.html"
    success_url = '#reviews'

    def get_context_data(self, **kwargs):
        kwargs['foods_list'] = Foods.objects.filter(in_menu=True).order_by('category')\
            .select_related('category', 'kitchen')
        return super(FoodsView, self).get_context_data(**kwargs)


class FoodsDetailView(DetailView):
    """Полное описание блюда"""
    model = Foods
    slug_field = 'url'


class KitchenDetailView(DetailView):
    """Описание кухни мира"""
    model = Kitchen
    slug_field = 'url'


class ChefsDetailView(DetailView):
    """Инфо о шеф-поваре"""
    model = Chefs
    slug_field = 'url'
