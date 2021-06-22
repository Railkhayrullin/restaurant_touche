from django import template
from restaurant.models import Category, Chef, Review, ContactInfo, RestaurantImage

register = template.Library()


@register.simple_tag()
def get_category():
    return Category.objects.exclude(pk=4)


@register.simple_tag()
def get_chefs():
    return Chef.objects.all()


@register.simple_tag()
def get_reviews(count=5):
    return Review.objects.filter(draft=False).order_by('-pk')[:count]


@register.simple_tag()
def get_contact_info():
    return ContactInfo.objects.all().first()


@register.simple_tag()
def get_restaurant_image():
    return RestaurantImage.objects.all()
