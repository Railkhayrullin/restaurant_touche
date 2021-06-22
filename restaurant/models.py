from django.db import models
from django.urls import reverse_lazy


class Category(models.Model):
    """Категории блюда в меню"""
    name = models.CharField("категория", max_length=100, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Kitchen(models.Model):
    """Кухни мира"""
    name = models.CharField("кухня", max_length=100, blank=False)
    description = models.TextField("описание", max_length=1000, blank=False)
    image = models.ImageField("изображение", upload_to='kitchen/', default='no_image.jpg')
    url = models.SlugField("ссылка", max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('kitchen', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "кухня мира"
        verbose_name_plural = "кухни мира"


class Food(models.Model):
    """Блюда в меню"""
    name = models.CharField("блюдо", max_length=100, blank=False)
    description = models.TextField("описание", blank=False)
    category = models.ForeignKey(Category, verbose_name='категория блюда', on_delete=models.SET_NULL, null=True,
                                 blank=False)
    kitchen = models.ForeignKey(Kitchen, verbose_name='кухня мира', on_delete=models.SET_NULL, null=True, blank=False)
    price = models.PositiveSmallIntegerField("цена", default=0, help_text='указывать сумму в рублях')
    image = models.ImageField("изображение", upload_to='food/', default='no_image.jpg')
    url = models.SlugField("ссылка", max_length=100, unique=True, blank=False)
    in_menu = models.BooleanField("показывать в меню", default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('food', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "блюдо"
        verbose_name_plural = "блюда"


class Chef(models.Model):
    """Шеф-повара"""
    name = models.CharField("шеф-повар", max_length=50, blank=False)
    age = models.PositiveSmallIntegerField("возраст", blank=False)
    description = models.TextField("описание", max_length=300, blank=False)
    kitchen = models.ManyToManyField(Kitchen, verbose_name='кухня мира', blank=False)
    image = models.ImageField("фото шеф-повара", upload_to='chefs/', blank=False)
    url = models.SlugField("ссылка", max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('chefs', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "шеф-повар"
        verbose_name_plural = "шеф-повара"


class Review(models.Model):
    """Отзывы"""
    name = models.CharField("имя", max_length=100, blank=False)
    email = models.EmailField("email", max_length=100, blank=False)
    message = models.TextField("сообщение", max_length=200, blank=False)
    draft = models.BooleanField("черновик", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"


class ContactInfo(models.Model):
    """Контактная информация"""
    city_postcode = models.CharField("город и почтовый индекс", max_length=100, default='')
    street_building = models.CharField("улица и номер здания", max_length=100, default='')
    from_hour_mon_thurs = models.TimeField("время открытия Пн-Чт", default='10:00:00', blank=False)
    to_hour_mon_thurs = models.TimeField("время закрытия Пн-Чт", default='23:00:00', blank=False)
    from_hour_fri_sun = models.TimeField("время открытия Пт-Вс", default='11:00:00', blank=False)
    to_hour_fri_sun = models.TimeField("время закрытия Пт-Вс", default='02:00:00', blank=False)
    contact_phone = models.CharField("контактный номер", max_length=16, blank=False)
    reservation_phone = models.CharField("номер для бронирования столиков", max_length=16, blank=False)
    email = models.EmailField("email", max_length=100, blank=False)

    def __str__(self):
        return self.city_postcode

    class Meta:
        verbose_name = "контактная информация"
        verbose_name_plural = "контактная информация"


class RestaurantImage(models.Model):
    """Фото ресторана"""
    name = models.CharField("имя", max_length=100, blank=False)
    image = models.ImageField("фото ресторана", upload_to='restaurant_image/', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "фото ресторана"
        verbose_name_plural = "фото ресторана"
