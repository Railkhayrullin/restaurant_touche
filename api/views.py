from rest_framework.viewsets import ModelViewSet
from .serializers import FoodSerializer

from restaurant.models import Food


class FoodView(ModelViewSet):
    queryset = Food.objects.filter(in_menu=True)\
                           .order_by('category')\
                           .select_related('category', 'kitchen')
    serializer_class = FoodSerializer
