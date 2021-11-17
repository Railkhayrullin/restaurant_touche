from django.db import models
from django.urls import reverse_lazy


class Kitchen(models.Model):
    """Кухни мира"""
    class Meta:
        verbose_name = "кухня мира"
        verbose_name_plural = "кухни мира"

    name = models.CharField("кухня", max_length=128)
    description = models.TextField("описание", max_length=1024)
    image = models.ImageField("изображение", upload_to='kitchen/', default='no_image.jpg')
    url = models.SlugField("ссылка", max_length=128, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('kitchen', kwargs={'slug': self.url})
