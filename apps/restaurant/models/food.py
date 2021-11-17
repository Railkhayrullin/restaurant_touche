from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse_lazy


class Food(models.Model):
    """Блюда в меню"""
    class Meta:
        verbose_name = "блюдо"
        verbose_name_plural = "блюда"
        constraints = [
            UniqueConstraint(fields=['name'], name='unique_food')
        ]

    name = models.CharField("блюдо", max_length=128)
    description = models.TextField("описание", max_length=2048)
    category = models.ForeignKey(to='restaurant.Category', verbose_name='категория блюда',
                                 on_delete=models.SET_NULL, null=True)
    kitchen = models.ForeignKey(to='restaurant.Kitchen', verbose_name='кухня мира',
                                on_delete=models.SET_NULL, null=True)
    price = models.PositiveSmallIntegerField("цена", default=0, help_text='указывать сумму в рублях')
    image = models.ImageField("изображение", upload_to='food/', default='no_image.jpg')
    url = models.SlugField("ссылка", max_length=128, unique=True)
    in_menu = models.BooleanField("показывать в меню", default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('food', kwargs={'slug': self.url})
