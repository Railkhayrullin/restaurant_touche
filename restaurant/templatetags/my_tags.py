from django import template
from restaurant.models import Category, Chefs, Reviews, ContactInfo, RestaurantImage

register = template.Library()


@register.simple_tag()
def get_category():
    return Category.objects.exclude(pk=4)


@register.simple_tag()
def get_chefs():
    return Chefs.objects.all()


@register.simple_tag()
def get_reviews(count=5):
    return Reviews.objects.filter(draft=False).order_by('-pk')[:count]


@register.simple_tag()
def get_contact_info():
    return ContactInfo.objects.all().first()


@register.simple_tag()
def get_restaurant_image():
    return RestaurantImage.objects.all()
