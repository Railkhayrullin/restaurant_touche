from django.db import models


class Review(models.Model):
    """Отзывы"""
    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"

    name = models.CharField("имя", max_length=128)
    email = models.EmailField("email", max_length=128)
    message = models.TextField("сообщение", max_length=512)
    draft = models.BooleanField("черновик", default=True)

    def __str__(self):
        return self.name
