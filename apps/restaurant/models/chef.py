from django.db import models
from django.urls import reverse_lazy


class Chef(models.Model):
    """Шеф-повара"""
    class Meta:
        verbose_name = "шеф-повар"
        verbose_name_plural = "шеф-повара"

    name = models.CharField("шеф-повар", max_length=64)
    age = models.PositiveSmallIntegerField("возраст")
    description = models.TextField("описание", max_length=512)
    kitchen = models.ManyToManyField(to='restaurant.Kitchen', verbose_name='кухня мира')
    image = models.ImageField("фото шеф-повара", upload_to='chefs/')
    url = models.SlugField("ссылка", max_length=128, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('chefs', kwargs={'slug': self.url})
