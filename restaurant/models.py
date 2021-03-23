from django.db import models
from django.urls import reverse_lazy


class Category(models.Model):
    """Категории блюда в меню"""
    name = models.CharField("Категория", max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Kitchen(models.Model):
    """Кухни мира"""
    name = models.CharField("Кухня", max_length=100, blank=False)
    description = models.TextField("Описание", max_length=1000, blank=False)
    image = models.ImageField("Изображение", upload_to='kitchen/', default='no_image.jpg')
    url = models.SlugField("Ссылка", max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('kitchen', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Кухня мира"
        verbose_name_plural = "Кухни мира"


class Foods(models.Model):
    """Блюда в меню"""
    name = models.CharField("Блюдо", max_length=100, blank=False)
    description = models.TextField("Описание", blank=False)
    category = models.ForeignKey(Category, verbose_name='Категория блюда', on_delete=models.SET_NULL, null=True,
                                 blank=False)
    kitchen = models.ForeignKey(Kitchen, verbose_name='Кухня мира', on_delete=models.SET_NULL, null=True, blank=False)
    price = models.PositiveSmallIntegerField("Цена", default=0, help_text='указывать сумму в рублях')
    image = models.ImageField("Изображение", upload_to='food/', default='no_image.jpg')
    url = models.SlugField("Ссылка", max_length=100, unique=True, blank=False)
    in_menu = models.BooleanField("Показывать в меню", default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('food', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"


class Chefs(models.Model):
    """Шеф-повара"""
    name = models.CharField("Шеф-повар", max_length=50, blank=False)
    age = models.PositiveSmallIntegerField("Возраст", blank=False)
    description = models.TextField("Описание", max_length=300, blank=False)
    kitchen = models.ManyToManyField(Kitchen, verbose_name='Кухня мира', blank=False)
    image = models.ImageField("Фото шеф-повара", upload_to='chefs/', blank=False)
    url = models.SlugField("Ссылка", max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('chefs', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Шеф-повар"
        verbose_name_plural = "Шеф-повара"


class Reviews(models.Model):
    """Отзывы"""
    name = models.CharField("Имя", max_length=100, blank=False)
    email = models.EmailField("Email", max_length=100, blank=False)
    message = models.TextField("Сообщение", max_length=200, blank=False)
    draft = models.BooleanField("Черновик", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class ContactInfo(models.Model):
    """Контактная информация"""
    city_postcode = models.CharField("Город и почтовый индекс", max_length=100, default='')
    street_building = models.CharField("Улица и номер здания", max_length=100, default='')
    from_hour_mon_thurs = models.TimeField("Время открытия Пн-Чт", default='10:00:00', blank=False)
    to_hour_mon_thurs = models.TimeField("Время закрытия Пн-Чт", default='23:00:00', blank=False)
    from_hour_fri_sun = models.TimeField("Время открытия Пт-Вс", default='11:00:00', blank=False)
    to_hour_fri_sun = models.TimeField("Время закрытия Пт-Вс", default='02:00:00', blank=False)
    contact_phone = models.CharField("Контактный номер", max_length=16, blank=False)
    reservation_phone = models.CharField("Номер для бронирования столиков", max_length=16, blank=False)
    email = models.EmailField("Email", max_length=100, blank=False)

    def __str__(self):
        return self.city_postcode

    class Meta:
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"


class RestaurantImage(models.Model):
    """Фото ресторана"""
    name = models.CharField("Имя", max_length=100, blank=False)
    image = models.ImageField("Фото ресторана", upload_to='restaurant_image/', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фото ресторана"
        verbose_name_plural = "Фото ресторана"

