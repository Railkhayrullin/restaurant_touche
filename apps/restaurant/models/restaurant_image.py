from django.db import models


class RestaurantImage(models.Model):
    """Фото ресторана"""
    class Meta:
        verbose_name = "фото ресторана"
        verbose_name_plural = "фото ресторана"

    name = models.CharField("имя", max_length=128)
    image = models.ImageField("фото ресторана", upload_to='restaurant_image/')

    def __str__(self):
        return self.name
