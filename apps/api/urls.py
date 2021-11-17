from rest_framework.routers import SimpleRouter
from .views import FoodView


router = SimpleRouter()

router.register('food', FoodView)

urlpatterns = []

urlpatterns += router.urls
