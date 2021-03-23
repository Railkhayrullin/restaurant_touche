from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, ContactInfo, Kitchen, Reviews, Foods, Chefs, RestaurantImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('id', 'name')
    list_display_links = ('name',)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    """Контактная информация"""
    list_display = ("id", "contact_phone", "reservation_phone", "email")
    list_editable = ("contact_phone", "reservation_phone", "reservation_phone")
    fieldsets = (
        (None, {
            "fields": (("city_postcode", "street_building"),
                       ("from_hour_mon_thurs", "to_hour_mon_thurs"),
                       ("from_hour_fri_sun", "to_hour_fri_sun"),
                       "contact_phone",
                       "reservation_phone",
                       "email",
                       )
        }),
    )

    def has_add_permission(self, request):
        """Функция не дает добавлять объектов больше, чем 'max_objects' """
        max_objects = 1
        if self.model.objects.count() >= max_objects:
            return False
        return super().has_add_permission(request)


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    """Кухни мира"""
    list_display = ("id", "name", "url")
    list_display_links = ("name",)
    prepopulated_fields = {"url": ("name",)}


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("id", "name", "email", "draft")
    list_display_links = ("name",)
    list_editable = ("draft",)


@admin.register(Foods)
class FoodsAdmin(admin.ModelAdmin):
    """Блюда в меню"""
    list_display = ("id", "name", "category", "kitchen", "price", "in_menu")
    list_display_links = ("name",)
    list_filter = ("category", "kitchen", "in_menu")
    search_fields = ("name", "kitchen__name")
    list_editable = ("price", "in_menu")
    readonly_fields = ('get_image',)
    prepopulated_fields = {"url": ("name",)}
    save_on_top = True
    save_as = True
    actions = ["published", "unpublished"]
    fieldsets = (
        (None, {
            "fields": (("name", "url"),
                       ("image", "get_image"),
                       "description",
                       ("category", "kitchen", "price"),
                       "in_menu",
                       )
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="120" height="80">')

    def unpublished(self, request, queryset):
        """Скрыть в меню"""
        row_update = queryset.update(in_menu=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей  были обновлены"
        self.message_user(request, f"{message_bit}")

    def published(self, request, queryset):
        """Показывать в меню"""
        row_update = queryset.update(in_menu=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей  были обновлены"
        self.message_user(request, f"{message_bit}")

    published.short_description = "Показать в меню"
    published.allowed_permissions = ("change",)

    unpublished.short_description = "Скрыть в меню"
    unpublished.allowed_permissions = ("change",)

    get_image.short_description = "Фото блюда"


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("id", "name", "age", "get_image")
    list_display_links = ("name",)
    list_editable = ("age",)
    prepopulated_fields = {"url": ("name",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="80" height="100">')

    get_image.short_description = "Фото"


@admin.register(RestaurantImage)
class RestaurantImageAdmin(admin.ModelAdmin):
    """Фото ресторана"""
    list_display = ("id", "name", "get_image")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="90" height="60">')

    get_image.short_description = "Фото ресторана"
